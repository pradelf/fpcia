# Import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


def set_jedha_template():
    """Set Jedha color palette as default for plotly visualizations"""
    # setting Jedha color palette as default
    pio.templates["jedha"] = go.layout.Template(
        layout_colorway=[
            "#4B9AC7",
            "#4BE8E0",
            "#9DD4F3",
            "#97FBF6",
            "#2A7FAF",
            "#23B1AB",
            "#0E3449",
            "#015955",
        ]
    )
    pio.templates.default = "jedha"
    pio.renderers.default = "vscode"  # to be replaced by "iframe" if working on JULIE
    pass
