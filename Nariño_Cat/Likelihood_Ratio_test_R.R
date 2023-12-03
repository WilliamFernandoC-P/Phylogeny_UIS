# Valores de log-likelihood
loglik_null <- -833.2514
loglik_alt <- -899.1985

# Calcular la estadística de prueba LRT
lrt_statistic <- -2 * (loglik_null - loglik_alt)

# Grados de libertad 
degrees_of_freedom <- 1

# Calcular el valor p
p_value <- 1 - pchisq(lrt_statistic, df = degrees_of_freedom)

# Interpretar el resultado
if (p_value < 0.05) {
  cat("Rechazamos el modelo nulo a favor del modelo alternativo.")
} else {
  cat("No hay evidencia para rechazar el modelo nulo.")
}
# Imprimir la estadística de prueba y el valor p
cat("Estadística de prueba LRT:", lrt_statistic, "\n")
cat("Valor p:", p_value, "\n")
