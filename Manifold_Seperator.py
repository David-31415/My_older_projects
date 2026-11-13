import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.widgets import Slider
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_moons
from sklearn.decomposition import PCA

#hyperparameters to change
torch.manual_seed(7654)
epochs = 200
lr = 0.01
snapshot_every = 1   # how often (in epochs) for an animation frame
m = 16                # width of the hidden layers



plt.style.use("dark_background")
CLASS_COLORS = ["#ff5d73", "#36c5f0"]   # class 0 = pink-red, class 1 = sky blue
CLASS_CMAP = ListedColormap(CLASS_COLORS)
POS_COLOR = "#00e0c6"   
NEG_COLOR = "#c77dff" 
ACCENT = "#FFDF00"     
SAVE_GIF = False      


X_np, Y_np = make_moons(n_samples=1000, noise=0.1, random_state=0)
X = torch.tensor(X_np, dtype=torch.float32)
Y = torch.tensor(Y_np, dtype=torch.float32).unsqueeze(1)
class_of_point = Y_np   

X_train, X_test = X[:800], X[800:]
Y_train, Y_test = Y[:800], Y[800:]



class DeepNN(nn.Module):
    def __init__(self, m, epochs, lr, snapshot_every):
        super().__init__()
        self.m = m
        self.epochs = epochs
        self.lr = lr
        self.snapshot_every = snapshot_every

        self.feature_extractor = nn.Sequential(
            nn.Linear(2, m), nn.Tanh(),
            nn.Linear(m, m), nn.Tanh(),
            nn.Linear(m, 2), nn.Tanh(),
        )
        self.classifier = nn.Linear(2, 1)
        self.model = nn.Sequential(self.feature_extractor, self.classifier)

        # the four weight matrices, left to right in the diagram
        self.weight_layers = [self.feature_extractor[0], self.feature_extractor[2],
                              self.feature_extractor[4], self.classifier]

        self.loss_fn = nn.BCEWithLogitsLoss()   #binary cross entropy with a sigmoid implicit
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)

    def forward(self, inputs):
        return self.model(inputs)

    # --- reading the current state of the network ---------------------------
    def hidden_activations(self):
        """The data as seen after each Tanh: [layer1 (m-D), layer2 (m-D), layer3 (2-D)]."""
        with torch.no_grad():
            acts = []
            h=X
            for layer in self.feature_extractor:
                h = layer(h)
                if isinstance(layer, nn.Tanh):
                    acts.append(h.numpy())
        return acts

    def classifier_line(self):
        #The line  w0*x + w1*y + b = 0  that the final classifier draws.
        w = self.classifier.weight.detach().numpy()[0]
        b = self.classifier.bias.detach().numpy()[0]
        return w, b

    def current_weights(self):
        return [layer.weight.detach().numpy().copy() for layer in self.weight_layers]

    def test_accuracy(self):
        with torch.no_grad():
            preds = (torch.sigmoid(self.model(X_test)) > 0.5).float()
        return float((preds == Y_test).float().mean().item())

    # training methods
    def take_snapshot(self, epoch):
        self.snap_epoch.append(epoch)
        self.snap_acts.append(self.hidden_activations())
        self.snap_line.append(self.classifier_line())
        self.snap_weights.append(self.current_weights())
        self.snap_acc.append(self.test_accuracy())

    def fit(self):
        self.snap_epoch = []
        self.snap_acts = []      # hidden activations per layer
        self.snap_line = []      # classifier line (w, b)
        self.snap_weights = []   # the four weight matrices
        self.snap_acc = []       # test accuracy

        self.take_snapshot(0)   
        for epoch in range(1, self.epochs + 1):
            self.optimizer.zero_grad()
            loss = self.loss_fn(self.model(X_train), Y_train)
            loss.backward()
            self.optimizer.step()
            if epoch % self.snapshot_every == 0:
                self.take_snapshot(epoch)

        self.num_frames = len(self.snap_epoch)
        self.num_layers = len(self.snap_acts[0])     
        self.num_groups = len(self.weight_layers)   


model = DeepNN(m, epochs, lr, snapshot_every)
model.fit()

snap_epoch = model.snap_epoch
snap_acts = model.snap_acts
snap_line = model.snap_line
snap_weights = model.snap_weights
snap_acc = model.snap_acc
num_frames = model.num_frames
num_layers = model.num_layers
num_groups = model.num_groups


layer_dims = [snap_acts[0][i].shape[1] for i in range(num_layers)]

points_per_frame = []
for acts in snap_acts:
    frame_points = []
    for i in range(num_layers):
        a = acts[i]
        if layer_dims[i] > 2:
            frame_points.append(PCA(n_components=2).fit_transform(a))
        else:
            frame_points.append(a)
    points_per_frame.append(frame_points)




panel_limits = []
for i in range(num_layers):
    layer_points = []
    for frame in range(num_frames):
        layer_points.append(points_per_frame[frame][i])
    all_points = np.concatenate(layer_points)
    xs, ys = all_points[:, 0], all_points[:, 1]
    margin_x = 0.08 * (xs.max() - xs.min() + 1e-6)
    margin_y = 0.08 * (ys.max() - ys.min() + 1e-6)
    panel_limits.append((xs.min() - margin_x, xs.max() + margin_x,
                         ys.min() - margin_y, ys.max() + margin_y))


weight_scale = []
for g in range(num_groups):
    biggest = 1e-9
    for weights in snap_weights:
        biggest = max(biggest, np.abs(weights[g]).max())
    weight_scale.append(biggest)




#Claude's beautiful visualiization:
def edge_style(weight, scale):
    """A weight -> (color, alpha, linewidth). Sign picks color, size picks thickness."""
    strength = min(abs(weight) / scale, 1.0)   # 0 (weak) .. 1 (strongest)
    color = POS_COLOR if weight >= 0 else NEG_COLOR
    alpha = 0.06 + 0.9 * strength
    width = 0.3 + 6.0 * strength ** 1.4
    return color, alpha, width


def plot_points(ax, points):
    return ax.scatter(points[:, 0], points[:, 1], c=class_of_point, cmap=CLASS_CMAP,
                      vmin=0, vmax=1, s=22, alpha=0.9, edgecolors="white", linewidths=0.3)


def style_panel(ax, title, limits=None):
    ax.set_title(title, fontsize=12, pad=8)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_edgecolor("#444")
    if limits is not None:
        x0, x1, y0, y1 = limits
        ax.set_xlim(x0, x1)
        ax.set_ylim(y0, y1)


def node_positions():
    """(x, y) screen positions for every neuron, grouped by layer."""
    sizes = [2, m, m, 2, 1]
    x_of_layer = np.linspace(0.06, 0.94, len(sizes))
    layers = []
    for size, x in zip(sizes, x_of_layer):
        ys = np.linspace(0.78, 0.22, size) if size > 1 else np.array([0.5])
        layers.append([(x, y) for y in ys])
    return layers, x_of_layer


def draw_network(ax):
    """Draw the schematic. Returns a flat list of (line, group, out_index, in_index)."""
    layers, x_of_layer = node_positions()
    labels = ["input\n(x, y)", "Linear+Tanh", "Linear+Tanh", "2-D projection", "output"]

    # one line per weight; keep a handle so we can recolor it every frame
    edges = []
    init_weights = snap_weights[0]
    for g in range(num_groups):
        W = init_weights[g]   # shape (out, in)
        for in_i, (x0, y0) in enumerate(layers[g]):
            for out_j, (x1, y1) in enumerate(layers[g + 1]):
                color, alpha, width = edge_style(W[out_j, in_i], weight_scale[g])
                (line,) = ax.plot([x0, x1], [y0, y1], color=color,
                                  alpha=alpha, lw=width, zorder=1)
                edges.append((line, g, out_j, in_i))

    # neurons as round dots (scatter markers stay circular at any aspect ratio)
    for layer, label, x in zip(layers, labels, x_of_layer):
        xs = [pos[0] for pos in layer]
        ys = [pos[1] for pos in layer]
        ax.scatter(xs, ys, s=150, c="#e8e8f0", edgecolors="#222", linewidths=0.8, zorder=3)
        ax.text(x, 0.07, label, ha="center", va="center", fontsize=9, color="#cfcfe0")

    # legend for what the edges mean
    ax.text(0.0, 0.62, "positive weight", color=POS_COLOR, fontsize=8.5, va="center")
    ax.text(0.0, 0.55, "negative weight", color=NEG_COLOR, fontsize=8.5, va="center")
    ax.text(0.0, 0.48, "thickness = strength", color="#9a9ab0", fontsize=8.5, va="center")

    # live classifier weights + bias, shown under the output neuron (filled in by update)
    out_x = x_of_layer[-1]
    out_weight_text = ax.text(out_x, 0.36, "", ha="center", va="top",
                              fontsize=9, color="#cfcfe0", family="monospace")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return edges, out_weight_text


# ---------------------------------------------------------------------------
# figure layout: network diagram on top, the four panels below
# ---------------------------------------------------------------------------
fig = plt.figure(figsize=(20, 10))
fig.patch.set_facecolor("#0d0d12")
gs = fig.add_gridspec(2, 4, height_ratios=[0.85, 1.0], hspace=0.22, wspace=0.12,
                      left=0.03, right=0.97, top=0.88, bottom=0.12)

suptitle = fig.suptitle("", fontsize=20, fontweight="bold", color="white", y=0.975)
caption = (f"feature extractor (2 \u2192 {m} \u2192 {m} \u2192 2) untangles the data, "
           f"then a single line classifies it    \u2014    make_moons \u00b7 tanh \u00b7 Adam")
fig.text(0.5, 0.035, caption, ha="center", fontsize=11, color="#9a9ab0")

ax_net = fig.add_subplot(gs[0, :])
ax_net.set_facecolor("#0d0d12")
edges, out_weight_text = draw_network(ax_net)

ax_input = fig.add_subplot(gs[1, 0])
ax_layer1 = fig.add_subplot(gs[1, 1])
ax_layer2 = fig.add_subplot(gs[1, 2])
ax_layer3 = fig.add_subplot(gs[1, 3])
ax_layers = [ax_layer1, ax_layer2, ax_layer3]
for ax in [ax_input] + ax_layers:
    ax.set_facecolor("#15151c")

# decision-region shading behind the bottleneck points: which side -> which class.
# the classifier predicts class 1 where  w0*x + w1*y + b > 0, class 0 otherwise.
bx0, bx1, by0, by1 = panel_limits[2]
region_gx, region_gy = np.meshgrid(np.linspace(bx0, bx1, 200),
                                   np.linspace(by0, by1, 200))
region_img = ax_layer3.imshow(np.zeros_like(region_gx), extent=(bx0, bx1, by0, by1),
                              origin="lower", cmap=CLASS_CMAP, vmin=0, vmax=1,
                              alpha=0.18, zorder=0, aspect="auto")

# input panel never changes
plot_points(ax_input, X.numpy())
pad = 0.1
style_panel(ax_input, "input space",
            (X[:, 0].min() - pad, X[:, 0].max() + pad,
             X[:, 1].min() - pad, X[:, 1].max() + pad))

# the three animated hidden-layer panels
layer_scatters = []
titles = ["hidden layer 1", "hidden layer 2", "2-D projection"]   # layer 3 title gets the live equation in update()
for i, ax in enumerate(ax_layers):
    layer_scatters.append(plot_points(ax, points_per_frame[0][i]))
    if layer_dims[i] <= 2:
        title = titles[i]   # already 2-D, no projection note needed
    else:
        title = f"{titles[i]}  ({layer_dims[i]}-D \u2192 PCA)"
    style_panel(ax, title, panel_limits[i])

# the classifier's separating line lives in the last panel
(decision_line,) = ax_layer3.plot([], [], color=ACCENT, ls="--", lw=2.2, zorder=3)


def update(frame):
    # move the points in each hidden-layer panel
    for i in range(num_layers):
        layer_scatters[i].set_offsets(points_per_frame[frame][i])

    # redraw the classifier line in the last panel, and show its slope-intercept form
    w, b = snap_line[frame]
    x0, x1, _, _ = panel_limits[2]
    x_line = np.linspace(x0, x1, 200)
    if abs(w[1]) > 1e-6:
        slope = -w[0] / w[1]
        intercept = -b / w[1]
        decision_line.set_data(x_line, slope * x_line + intercept)
        sign = "+" if intercept >= 0 else "-"
        ax_layer3.set_title(f"2-D projection:   y = {slope:.2f}x {sign} {abs(intercept):.2f}",
                            fontsize=12, pad=8)
    else:
        decision_line.set_data([], [])
        ax_layer3.set_title("2-D projection:   vertical decision line", fontsize=12, pad=8)

    # live classifier weights + bias under the output neuron
    out_weight_text.set_text(f"w = [{w[0]:+.2f}, {w[1]:+.2f}]\nb = {b:+.2f}")

    # shade the two decision regions in the bottleneck panel
    region_img.set_data((w[0] * region_gx + w[1] * region_gy + b > 0).astype(float))

    # recolor / resize every edge from this frame's weights
    weights = snap_weights[frame]
    for line, g, out_j, in_i in edges:
        color, alpha, width = edge_style(weights[g][out_j, in_i], weight_scale[g])
        line.set_color(color)
        line.set_alpha(alpha)
        line.set_linewidth(width)

    suptitle.set_text(f"Deep NN learning to untangle a manifold  \u2014   "
                      f"epoch {snap_epoch[frame]:>4}   \u2014   "
                      f"test accuracy {snap_acc[frame]:5.1%}")

    # keep the slider in sync when the animation advances (without re-firing on_changed)
    if not slider_syncing[0]:
        slider_syncing[0] = True
        epoch_slider.set_val(frame)
        slider_syncing[0] = False

    return (layer_scatters + [decision_line, out_weight_text, region_img]
            + [edge[0] for edge in edges])


# epoch scrubber — drag to jump; pauses the auto-play animation
ax_slider = fig.add_axes([0.08, 0.055, 0.84, 0.018], facecolor="#1a1a24")
epoch_slider = Slider(ax_slider, "epoch", 0, num_frames - 1, valinit=0, valstep=1,
                      color=ACCENT, track_color="#3a3a4a", handle_style={"facecolor": ACCENT})
slider_syncing = [False]   # mutable flag so set_val during animation doesn't loop


def on_epoch_slider(val):
    if slider_syncing[0]:
        return
    anim.event_source.stop()
    frame = int(val)
    update(frame)
    epoch_slider.valtext.set_text(str(snap_epoch[frame]))
    fig.canvas.draw_idle()


epoch_slider.on_changed(on_epoch_slider)
update(0)
epoch_slider.valtext.set_text(str(snap_epoch[0]))

anim = FuncAnimation(fig, update, frames=num_frames, interval=80, blit=False, repeat=True)

try:
    manager = plt.get_current_fig_manager() #full screen
    manager.full_screen_toggle()
except Exception as e:
    print("full screen toggle failed:", e)


if SAVE_GIF:
    out = "untangling.gif"
    # subsample frames so the GIF stays a reasonable size for posting
    max_gif_frames = 150
    stride = max(1, num_frames // max_gif_frames)
    gif_indices = list(range(0, num_frames, stride))
    gif_anim = FuncAnimation(fig, update, frames=gif_indices, interval=80, blit=False)
    gif_anim.save(out, writer=PillowWriter(fps=18), dpi=64)
    # shrink further: re-encode with an optimized palette
    try:
        from PIL import Image, ImageSequence
        im = Image.open(out)
        gif_frames = [f.copy() for f in ImageSequence.Iterator(im)]
        gif_frames[0].save(out, save_all=True, append_images=gif_frames[1:],
                           loop=0, duration=im.info.get("duration", 55),
                           optimize=True, disposal=2)
    except Exception as e:
        print("gif optimize skipped:", e)
    print(f"saved {out} ({len(gif_indices)} frames)")

plt.show()
