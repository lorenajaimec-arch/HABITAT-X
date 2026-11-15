# HABITAT-X v4 — Earth Analog Catalog for the Lunar South Pole, Arcadia, and Utopia
# Run in Google Colab. Sites and their categories are documented
# with references, but NO physical similarity percentages are invented.
# "Coverage" is the percentage of relevant categories represented by
# each catalog entry. It is neither a probability nor a NASA measurement.

import gradio as gr
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

CATEGORIAS = [
    "Impacts and craters", "Volcanism and basalts", "Dust and regolith",
    "Ice and permafrost", "Extreme cold", "Aridity",
    "Minerals and sediments", "Terrain and mobility", "Mission operations"
]

REGIONES = {
    "Moon | South Pole": {
        "destination": "Moon",
        "target_categories": ["Impacts and craters", "Dust and regolith",
                      "Ice and permafrost", "Extreme cold",
                      "Terrain and mobility", "Mission operations"],
        "description": "Region of interest for Artemis: impact regolith, craters, permanently shadowed areas, potential water ice, and challenging slopes.",
        "source": "https://www.nasa.gov/news-release/nasa-provides-update-on-artemis-iii-moon-landing-regions/"
    },
    "Mars | Arcadia Planitia": {
        "destination": "Mars",
        "target_categories": ["Ice and permafrost", "Extreme cold", "Aridity",
                      "Dust and regolith", "Terrain and mobility",
                      "Mission operations"],
        "description": "Mid-latitude region with indications of subsurface ice and landforms potentially associated with ice.",
        "source": "https://www.usgs.gov/publications/geomorphological-evidence-near-surface-ice-candidate-landing-sites-northern-amazonis"
    },
    "Mars | Utopia Planitia": {
        "destination": "Mars",
        "target_categories": ["Ice and permafrost", "Extreme cold", "Aridity",
                      "Dust and regolith", "Minerals and sediments",
                      "Terrain and mobility", "Mission operations"],
        "description": "Vast Martian plain with radar-detected buried ice deposits and areas of polygonal terrain.",
        "source": "https://science.nasa.gov/resource/location-of-large-subsurface-water-ice-deposit-in-utopia-planitia-mars/"
    }
}

NASA = "https://science.nasa.gov/solar-system/planetary-analogs/"
USGS = "https://www.usgs.gov/media/images/common-analogs-northern-arizona"
EXPLORER = "https://science.nasa.gov/solar-system/analog-explorer/"
ESA = "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/CAVES_and_Pangaea/What_is_PANGAEA"
ESTUDIO = "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022JE007676"
NASA_H = "https://science.nasa.gov/solar-system/planetary-analogs/10-things-to-know-about-planetary-analogs/"
MARTE = "https://www.eppcgs.org/article/doi/10.26464/epp2022042"
QAIDAM = "https://academic.oup.com/edited-volume/62111/chapter-abstract/549107179"
LUT = "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023JF007417"

# Coordinates represent approximate points used to locate an area
# on the map, NOT exact experiment or landing coordinates.
sitios = []

def agregar(destino, nombre, pais, lat, lon, etiquetas, descripcion, fuente,
            certeza="Documented as an analog"):
    sitios.append({
        "Destination": destino, "Site": nombre, "Country": pais,
        "Latitude (°)": float(lat), "Longitude (°)": float(lon),
        "Categories": set(etiquetas.split("|")),
        "Application": descripcion, "Source": fuente, "Evidence status": certeza
    })

# ------------------ LUNAR ANALOG CATALOG -----------------------------
agregar("Moon","Cinder Lake Crater Field","United States",35.35,-111.48,
        "Impacts and craters|Dust and regolith|Terrain and mobility|Mission operations",
        "Traversal and mobility training among simulated craters.",USGS)
agregar("Moon","Meteor Crater","United States",35.03,-111.02,
        "Impacts and craters|Terrain and mobility",
        "Impact processes and recognition of crater structures.",USGS)
agregar("Moon","Black Point Lava Flow","United States",35.70,-111.65,
        "Volcanism and basalts|Terrain and mobility|Mission operations",
        "Mobility and operations testing on volcanic terrain.",USGS)
agregar("Moon","Sunset Crater","United States",35.37,-111.50,
        "Volcanism and basalts|Dust and regolith|Terrain and mobility",
        "Scoria, volcanic deposits, and geological testing.",USGS)
agregar("Moon","S P Mountain","United States",35.58,-111.63,
        "Volcanism and basalts|Terrain and mobility|Mission operations",
        "Volcanism and traverse planning on uneven terrain.",USGS)
agregar("Moon","Lava River Cave","United States",35.35,-111.82,
        "Volcanism and basalts|Ice and permafrost|Mission operations",
        "Study of lava tubes, microclimates, and resource detection.",USGS)
agregar("Moon","Lava Beds National Monument","United States",41.74,-121.52,
        "Volcanism and basalts|Mission operations",
        "Lava-tube reconnaissance methods.",NASA)
agregar("Moon","Kīlauea","United States",19.42,-155.29,
        "Volcanism and basalts|Terrain and mobility|Mission operations",
        "Basaltic landscape analog; does not reproduce polar ice.",EXPLORER)
agregar("Moon","Askja","Iceland",65.05,-16.75,
        "Ice and permafrost|Volcanism and basalts|Terrain and mobility",
        "Testing instruments designed to detect subsurface ice.",EXPLORER)
agregar("Moon","Lanzarote","Spain",29.05,-13.65,
        "Volcanism and basalts|Terrain and mobility|Mission operations",
        "Geology training for astronauts in the PANGAEA program.",ESA)
agregar("Moon","Nördlinger Ries Crater","Germany",48.88,10.58,
        "Impacts and craters|Mission operations",
        "Impact geology reconnaissance.",ESA)
agregar("Moon","Lofoten","Norway",68.21,13.61,
        "Minerals and sediments|Terrain and mobility|Mission operations",
        "Training to interpret lunar highland rock analogs.",ESA)
agregar("Moon","Haughton Crater","Canada",75.38,-89.68,
        "Impacts and craters|Extreme cold|Terrain and mobility|Mission operations",
        "Exploration, mobility, and operations in remote conditions.",NASA_H)
agregar("Moon","Grenville Province","Canada",46.80,-75.00,
        "Minerals and sediments",
        "Anorthositic massifs for comparison with lunar highland rocks.",ESTUDIO)
agregar("Moon","Mauna Kea","United States",19.82,-155.47,
        "Volcanism and basalts|Dust and regolith|Terrain and mobility|Mission operations",
        "Volcanic terrain for instrumentation and operational tests.",NASA)

# ------------------ MARTIAN ANALOG CATALOG --------------------------
agregar("Mars","Atacama Desert","Chile",-23.50,-68.20,
        "Aridity|Dust and regolith|Minerals and sediments|Mission operations",
        "Instrument testing and searches for biosignatures in extremely dry terrain.",EXPLORER)
agregar("Mars","McMurdo Dry Valleys","Antarctica",-77.50,162.00,
        "Extreme cold|Aridity|Ice and permafrost|Terrain and mobility",
        "Freezing processes and operations in polar deserts.",NASA)
agregar("Mars","Haughton Crater","Canada",75.38,-89.68,
        "Impacts and craters|Extreme cold|Terrain and mobility|Mission operations",
        "Operational trials, human exploration, and remote mobility.",NASA_H)
agregar("Mars","Hanksville (MDRS)","United States",38.41,-110.79,
        "Aridity|Minerals and sediments|Terrain and mobility|Mission operations",
        "Simulation of Martian mission activities and procedures.",
        "https://www.hanksvilleutah.gov/mars-on-earth")
agregar("Mars","Death Valley","United States",36.50,-116.87,
        "Aridity|Minerals and sediments|Terrain and mobility",
        "Testing on arid terrains and sedimentary deposits.",NASA)
agregar("Mars","Askja / Víkurssandur","Iceland",65.05,-16.75,
        "Volcanism and basalts|Terrain and mobility|Dust and regolith",
        "Study of ripples and volcanic sediments comparable to some Martian landforms.",EXPLORER)
agregar("Mars","Holuhraun","Iceland",64.88,-16.83,
        "Volcanism and basalts|Terrain and mobility",
        "Recent lava field for studying volcanic landforms.",
        "https://www.usgs.gov/")
agregar("Mars","Qaidam Basin","China",37.40,95.20,
        "Extreme cold|Aridity|Minerals and sediments|Dust and regolith",
        "High-altitude arid saline basin with sediments and wind-shaped landforms.",QAIDAM)
agregar("Mars","Rio Tinto","Spain",37.68,-6.56,
        "Minerals and sediments",
        "Study of hydrated minerals and geochemical processes.",ESTUDIO)
agregar("Mars","Andean Puna","Argentina",-24.20,-66.20,
        "Aridity|Extreme cold|Volcanism and basalts|Minerals and sediments",
        "High-altitude, dry, volcanic environments for environmental testing.",ESTUDIO)
agregar("Mars","Makgadikgadi","Botswana",-20.60,25.50,
        "Minerals and sediments|Aridity|Terrain and mobility",
        "Evaporite deposits and sedimentary landforms associated with ancient water.",ESTUDIO)
agregar("Mars","Craters of the Moon (Idaho)","United States",43.42,-113.52,
        "Volcanism and basalts|Terrain and mobility|Mission operations",
        "Basaltic rocks and lava terrain for geological testing.",MARTE)
agregar("Mars","Lut Desert","Iran",30.60,59.10,
        "Aridity|Dust and regolith|Terrain and mobility",
        "Sedimentary ripples and wind-shaped surfaces.",LUT)
agregar("Mars","Dallol (Danakil)","Ethiopia",14.24,40.30,
        "Minerals and sediments|Aridity",
        "Extreme saline and geochemical environments; not an ice analog.",MARTE)
agregar("Mars","Kangerlussuaq","Greenland",67.00,-50.70,
        "Ice and permafrost|Extreme cold",
        "Cold environment relevant to frozen subsurface studies and seismic measurements.",ESTUDIO)
agregar("Mars","Mojave Desert","United States",35.15,-116.10,
        "Aridity|Minerals and sediments|Terrain and mobility|Mission operations",
        "Dry terrain for mobility and geology tests.",NASA)
agregar("Mars","Lava Beds National Monument","United States",41.74,-121.52,
        "Volcanism and basalts|Mission operations",
        "Volcanic tube reconnaissance applicable to Mars exploration.",NASA)

CATALOGO = pd.DataFrame(sitios)
CATALOGO["Displayed categories"] = CATALOGO["Categories"].map(
    lambda s: ", ".join(sorted(s))
)

def explorar(region, categoria, modo, estilo_mapa):
    objetivo = REGIONES[region]
    grupo = objetivo["destination"]
    catalogo = CATALOGO[CATALOGO["Destination"] == grupo].copy()

    def presentes(row):
        return sorted(row["Categories"].intersection(objetivo["target_categories"]))

    catalogo["Matches"] = catalogo.apply(presentes, axis=1)
    catalogo["Category count"] = catalogo["Matches"].map(len)
    catalogo["Category coverage (%)"] = (
        100 * catalogo["Category count"] / len(objetivo["target_categories"])
    ).round(1)
    # Category coverage is NOT physical similarity or probability.
    catalogo["Matching categories"] = catalogo["Matches"].map(
        lambda arr: ", ".join(arr) if arr else "No documented matching category"
    )

    if categoria != "All":
        catalogo = catalogo[
            catalogo["Matches"].map(lambda a: categoria in a)
        ]

    if modo == "Single-category focus":
        catalogo["Sort group"] = catalogo["Category count"].map(lambda x: 1 if x > 0 else 0)
        catalogo = catalogo.sort_values(
            ["Sort group", "Site"], ascending=[False, True]
        )
    else:
        catalogo = catalogo.sort_values(
            ["Category coverage (%)", "Site"], ascending=[False, True]
        )

    if len(catalogo) == 0:
        return ("No sites with that documented category were found.",
                pd.DataFrame(), go.Figure(), go.Figure(), "")

    texto = (
        f"### {region}\n\n{objetivo['description']}\n\n"
        f"*{len(catalogo)} Earth analog sites match this filter.* "
        "*Sites matching only one category are not excluded.*\n\n"
        "Category coverage is the proportion of target categories "
        "supported by analog-use evidence; *it does not measure physical similarity*. "
        "An unmarked category means no evidence recorded, NOT 0% similarity.\n\n"
        f"[Source for the selected region]({objetivo['source']})"
    )

    visibles = catalogo[
        ["Site", "Country", "Category count", "Category coverage (%)",
         "Matching categories", "Application", "Source"]
    ].reset_index(drop=True)

    # Detailed map: free basemap styles without a Mapbox key.
    estilos = {
        "Space dark": "carto-darkmatter",
        "Scientific light": "carto-positron",
        "Exploration": "carto-voyager",
        "OpenStreetMap": "open-street-map"
    }
    mapa = px.scatter_map(
        catalogo,
        lat="Latitude (°)", lon="Longitude (°)",
        hover_name="Site",
        hover_data={
            "Country": True,
            "Matching categories": True,
            "Latitude (°)": ":.3f",
            "Longitude (°)": ":.3f",
            "Category coverage (%)": ":.1f"
        },
        color="Category count", size="Category count", size_max=23,
        color_continuous_scale="Turbo", zoom=0.8,
        center={"lat": 10, "lon": 0},
        map_style=estilos.get(estilo_mapa, "carto-darkmatter"),
        title=f"Earth analog sites · {region}"
    )
    mapa.update_traces(marker=dict(opacity=0.85))
    mapa.update_layout(
        height=620,
        margin=dict(l=0, r=0, t=55, b=0),
        font=dict(family="Arial", size=13, color="#E2E8F0"),
        paper_bgcolor="#0B1220",
        coloraxis_colorbar=dict(title="Categories", tickfont=dict(color="#E2E8F0")),
        title_font=dict(color="#E2E8F0", size=18)
    )

    # Bars with consistent styling and visible labels.
    catalogo_ordenado = catalogo.sort_values("Category count")
    barras = px.bar(
        catalogo_ordenado,
        x="Category count", y="Site", orientation="h",
        color="Category count", color_continuous_scale="Turbo",
        title="Documented categories by Earth analog site",
        labels={"Category count": "Number of categories"}
    )
    barras.update_traces(
        texttemplate="%{x}", textposition="outside", marker_line_width=0,
        cliponaxis=False
    )
    barras.update_layout(
        template="plotly_dark", paper_bgcolor="#0B1220",
        plot_bgcolor="#0B1220", font=dict(color="#E2E8F0", size=12),
        xaxis=dict(title="Matching categories", gridcolor="#34445F",
                   range=[0, max(2, int(catalogo["Category count"].max()) + 1)]),
        yaxis=dict(title=""),
        showlegend=False, coloraxis_showscale=False,
        height=max(460, 32 * len(catalogo)),
        margin=dict(l=5, r=35, t=60, b=30)
    )

    detalles = "\n\n".join(
        f"*{r['Site']} ({r['Country']})* — {r['Matching categories']}. "
        f"{r['Application']} [Source]({r['Source']})"
        for _,r in catalogo.iterrows()
    )
    return texto, visibles, mapa, barras, detalles


def catalogo_por_destino(destino):
    t = CATALOGO[CATALOGO["Destination"] == destino][
        ["Site", "Country", "Displayed categories", "Application", "Source"]
    ].copy()
    return t.reset_index(drop=True)

def figura_demostrativa(escala="Earth"):
    """Illustrative 3D view: NOT measured elevation data."""
    x = np.linspace(-4, 4, 120)
    y = np.linspace(-4, 4, 120)
    X, Y = np.meshgrid(x, y)
    Z = (
        2.3*np.exp(-((X-1)**2+Y**2)/2)
        + 1.5*np.exp(-((X+1.5)**2+(Y+1)**2))
        + 0.3*np.sin(3*X)*np.cos(2*Y)
    )
    fig = go.Figure(go.Surface(
        x=X, y=Y, z=Z,
        colorscale=escala, showscale=True,
        colorbar=dict(title="Relative height", tickfont=dict(color="#E2E8F0")),
        lighting=dict(ambient=0.45, diffuse=0.85,
                      specular=0.25, roughness=0.65),
        lightposition=dict(x=100, y=200, z=500)
    ))
    fig.update_layout(
        title="Illustrative 3D Terrain (not measured data)",
        paper_bgcolor="#0B1220",
        font=dict(color="#E2E8F0", size=12),
        scene=dict(
            bgcolor="#0B1220",
            xaxis=dict(title="X (relative units)",
                       backgroundcolor="#101B30", gridcolor="#34445F"),
            yaxis=dict(title="Y (relative units)",
                       backgroundcolor="#101B30", gridcolor="#34445F"),
            zaxis=dict(title="Z (relative units)",
                       backgroundcolor="#101B30", gridcolor="#34445F"),
            camera=dict(eye=dict(x=1.7, y=1.7, z=1.2)),
            aspectratio=dict(x=1, y=1, z=0.55)
        ),
        height=610,
        margin=dict(l=0, r=0, t=55, b=0)
    )
    return fig

with gr.Blocks(title="HABITAT-X — Expanded Catalog") as demo:
    gr.Markdown("# 🚀 HABITAT-X")
    gr.Markdown("**The sites and reported analog applications are drawn from cited sources, "
                "without invented physical similarity percentages.** The classification by "
                "category is a research synthesis that the team can review.")
    with gr.Tab("🔎 Search by region and characteristic"):
        region = gr.Dropdown(list(REGIONES), value="Moon | South Pole",
                             label="Extraterrestrial region")
        categoria = gr.Dropdown(["All"] + CATEGORIAS,
                                value="All", label="Characteristic")
        modo = gr.Radio(["All testing categories", "Single-category focus"],
                         value="All testing categories", label="Search mode")
        estilo_mapa = gr.Dropdown(
            ["Space dark", "Scientific light", "Exploration", "OpenStreetMap"],
            value="Space dark", label="World map style"
        )
        boton = gr.Button("FIND ANALOG SITES", variant="primary")
        resumen = gr.Markdown()
        tabla = gr.Dataframe(label="Matching Earth analog catalog", interactive=False)
        mapa = gr.Plot(label="World map")
        barras = gr.Plot(label="Categories per location")
        detalles = gr.Markdown()
        boton.click(explorar, inputs=[region,categoria,modo,estilo_mapa],
                    outputs=[resumen,tabla,mapa,barras,detalles])
    with gr.Tab("🌙 Full lunar analog catalog"):
        gr.Markdown("Earth sites for lunar-related testing; not all reproduce "
                    "the specific conditions of the lunar South Pole.")
        gr.Dataframe(value=catalogo_por_destino("Moon"), interactive=False)
    with gr.Tab("🔴 Full Martian analog catalog"):
        gr.Markdown("Earth sites relevant to different aspects of Mars. "
                    "Arcadia and Utopia have different profiles and no identical Earth analog.")
        gr.Dataframe(value=catalogo_por_destino("Mars"), interactive=False)
    with gr.Tab("🏔️ 3D terrain view"):
        gr.Markdown("This surface remains illustrative. Showing "
                    "real terrain requires a digital elevation model (DEM) from a scientific source.")
        escala_3d = gr.Dropdown(
            ["Earth", "Viridis", "Turbo", "Cividis"],
            value="Earth", label="3D terrain color palette"
        )
        vista_3d = gr.Plot(value=figura_demostrativa())
        escala_3d.change(figura_demostrativa, inputs=escala_3d, outputs=vista_3d)
    gr.Markdown("*Limitations:* Marker coordinates are approximate. "
                "This catalog does not evaluate construction feasibility, gravity, "
                "vacuum, radiation, or exploration safety. "
                "Full coverage of a category means a documented category match, "
                "not physical identity between locations.")

if __name__ == "__main__":
    demo.launch()