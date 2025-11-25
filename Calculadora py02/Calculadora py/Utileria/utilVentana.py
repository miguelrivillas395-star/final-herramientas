def centrarVentana(ventana,aplicacionAncho,aplicacionLargo):
    pantallaAncho = ventana.winfo_screenwidth()
    pantallaLargo = ventana.winfo_screenheight()
    x = int((pantallaAncho/2) - (aplicacionAncho/2))
    y = int((pantallaLargo/2) - (aplicacionLargo/2))
    return ventana.geometry(f"{aplicacionAncho}x{aplicacionLargo}+{x}+{y}")