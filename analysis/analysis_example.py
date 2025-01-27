# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy",
#     "scipy",
#     "zooplotlib",
#     "zooplotly",
# ]
#
# [tool.uv.sources]
# zooplotlib = { git = "ssh://git@github.com/KittyCAD/zooplotlib.git" }
# zooplotly = { git = "ssh://git@github.com/KittyCAD/zooplotly.git" }
# ///

def create_example_plot() -> None:

    import matplotlib.pyplot as plt
    from zooplotlib import style

    style.use_zoo_style()

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3], label="data")
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    ax.set_title("Plot Title")
    ax.legend()

    plt.savefig("plot.png")
    plt.close()

if __name__ == "__main__":
    create_example_plot()