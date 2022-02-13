# ProyectoDash
Proyecto de Dash de la asignatura Visualización Avanzada del Master de Ciencia de Datos de la Universidad de Valencia.

## Cosas que podríamos incluir

- [ ] Visualizador de tipos de datos
- [ ] Visualizador de datos faltantes
- [ ] Cambios de escala
- [ ] Agrupación por alguna variable
- Tipos de plots
    - [ ] Scatter (Análisis bivariante)
    - [ ] Histograma (Comparación de tantas variables como queramos)
    - [ ] BoxPlots
    ]
- [x] Color en el scatter
- [x] Ajustados los dropdowns para que estén en la misma fila y añadido encima el texto de lo que corresponde cada uno

## Posibles cambios

- Igual es más fácil si los dropdowns y el plot aparecen a la vez. Le ponemos un valor inicial a los dropdowns y así el plot se puede dibujar. Algo como meterlo todo en un único `Div` o algo así.

- Podríamos probar a poner los dropwdowns en vertical y ponerles delante el texto en lugar de ponerlo arriba.

- Hechas algunas pruebas con el multipage y la verdad es que tiene buena pinta. El sistema que podríamos seguir es:
    1. Una vez se carga el df, se muestran algunas cosas básicas (como lo que aperecería con un `.describe()` y un `.info()`).
    2. Colocamos unos cuantos botones para elegir qué tipo de análisis queremos hacer (univariante, bivariante, etc) y colocamos esa página ahí.
  Es posible que esto también nos quitase algunos problemas con callbacks que esperan a que otras cosas aparezcan pero no han aparecido todavía, etc.

## Cosas a revisar

- [ ] Todas las veces en las que una figura depende de un dropdown que todavía no existe.