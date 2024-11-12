from modulo_pestagnas_abiertas.pestagnas_abiertas import PestagnasAbiertas

pestagnas_abiertas = PestagnasAbiertas()
pestagnas_abiertas.obtener_pestagna_actual().interpretar_comando("ir www.prueba2.com")
pestagnas_abiertas.obtener_pestagna_actual().interpretar_comando("atras")
pestagnas_abiertas.obtener_pestagna_actual().interpretar_comando("adelante")
pestagnas_abiertas.abrir_pestagna("www.prueba3.com")
pestagnas_abiertas.cambiar_pestagna(1)
pestagnas_abiertas.mostrar_pestagnas()
pestagnas_abiertas.abrir_pestagna("www.wikipedia.com")
pestagnas_abiertas.mostrar_pestagnas()
pestagnas_abiertas.cambiar_pestagna(2)
pestagnas_abiertas.cerrar_pestagna()
pestagnas_abiertas.mostrar_pestagnas()