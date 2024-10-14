def mcm(num1, num2):
  """Calcula el mínimo común múltiplo de dos números.

  Args:
    num1: Primer número.
    num2: Segundo número.

  Returns:
    El mínimo común múltiplo de num1 y num2.
  """

  # Encuentra el mayor número
  mayor = max(num1, num2)

  while True:
    if mayor % num1 == 0 and mayor % num2 == 0:
      return mayor
    mayor += 1

# Ejemplo de uso:
resultado = mcm(10, 20)
print("El MCM es:", resultado)