import bar_chart_race as bcr
import pandas as pd

#počáteční soubor pro pandas
df= pd.read_csv(r"D:\Python projekty a cvičení\bar_chart_race\data.csv", index_col="Date") 

# vyplnění prázdných dat v souboru dat na hodnotu 0.0
df.fillna(0.0, inplace=True)

#rozložení grafu
bcr.bar_chart_race(
    df=df[:5],

    #založení videa souboru
    filename="video.mp4",
    
    #základní složka s obrázky
    img_label_folder=(r"D:\Python projekty a cvičení\bar_chart_race\bar_image_labels"),
    fig_kwargs={
       #velikost souboru
        "figsize": (26, 15),
        "dpi": 120,

        #barba pozadí
        "facecolor": "#F8FAFF"
    },
    #prvních 10 řádků souboru
    n_bars=10,
    fixed_max=False,
    steps_per_period=45,
    
    #barva pozadí sloupců
    period_length=1500,
    colors=["#6ECBCE", "#FF2243", "#FFC33D", "#CE9673", "#FFA0FF", "#6501E5", "#F79522", "#699AF8", "#34718E", "#00DBCD",
        "#00A3FF", "#F8A737", "#56BD5B", "#D40CE5", "#6936F9", "#FF317B", "#0000F3", "#FFA0A0", "#31FF83", "#0556F3"
    ],

    #základní hlavička
    title={
        "label":"Top Computer Science Schools 2000-2020",
        "size":52,
        "weight":"bold",
        "pad": 40

    },

    #dedikované období
    period_label={
        "x":0.95, "y":0.15,
        "ha":"right","va":"center",
        "size": 72, "weight": "semibold"
    },
    bar_label_font={"size":27},
    tick_label_font={"size": 27},
    bar_kwargs={
        "alpha":0.99,
        "lw": 0
    },

    bar_texttemplate="{x:2f}",
    period_template="{x:.0f}"
)




