from dash import Dash, dcc
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout


def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Unemployment rate in US"
    app.layout = create_layout(app)
    app.run_server(debug=True, threaded=True)


if __name__ == "__main__":
    main()
