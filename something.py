from lets_plot import *
from palmerpenguins import load_penguins

LetsPlot.setup_html()

penguins = load_penguins()

plot = (
    ggplot(penguins, aes(x="flipper_length_mm", y="body_mass_g")) +
    geom_point(aes(color="species", shape="species")) +
    geom_smooth(method="lm") +
    labs(
        title="Body mass vs flipper length",
        x="Flipper length (mm)",
        y="Body mass (g)"
    )
)

ggsave(plot, filename="penguins_plot.html")