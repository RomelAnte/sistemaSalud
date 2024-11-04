(deffacts hechos-iniciales
    (tiene-fiebre)
    (tiene-dolor-de-garganta)
    (tiene-tos)
    (tiene-erupciones)
    (tiene-dolor-de-cabeza)
    (tiene-congestion-nasal)
)

(defrule gripe
    (tiene-fiebre)
    (tiene-tos)
    (tiene-congestion-nasal)
    =>
    (assert (es-gripe))
)

(defrule amigdalitis
    (tiene-fiebre)
    (tiene-dolor-de-garganta)
    =>
    (assert (es-amigdalitis))
)

(defrule sarampion
    (tiene-fiebre)
    (tiene-erupciones)
    =>
    (assert (es-sarampion))
)

(defrule migraña
    (tiene-dolor-de-cabeza)
    (tiene-fiebre)
    =>
    (assert (es-migraña))
)

(defrule resfriado-comun
    (tiene-congestion-nasal)
    (tiene-tos)
    =>
    (assert (es-resfriado-comun))
)
