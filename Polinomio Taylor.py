def factorial(n):
    """
    Calcula el factorial de un número entero de forma iterativa.
    Args:
        n (int): Número del cual se quiere calcular el factorial.
    Returns:
        int: El factorial de n.
    """
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def polinomio_taylor_seno(x, n):
    """
    Calcula la aproximación del seno usando el polinomio de Taylor centrado en x=0.
    
    Args:
        x (float): Valor en el cual se evalúa el seno.
        n (int): Número de términos del polinomio de Taylor a usar.
    
    Returns:
        float: Aproximación del seno de x.
    """
    seno_aprox = 0.0
    potencia = x  # x^(2k+1), empieza en x^1
    fact = 1      # (2k+1)!, empieza en 1!
    signo = 1     # (-1)^k, empieza positivo

    for k in range(n):
        termino = signo * potencia / fact
        seno_aprox += termino

        # Preparar el siguiente término
        signo *= -1
        potencia *= x * x  # x^(2k+3) = x^(2k+1) * x^2
        fact *= (2 * k + 2) * (2 * k + 3)  # (2k+3)! = (2k+1)! * (2k+2)*(2k+3)

    return seno_aprox
print(polinomio_taylor_seno(0, 5))        # 0.0
print(polinomio_taylor_seno(1, 10))       # ≈ 0.8414709848078965
print(polinomio_taylor_seno(-1, 7))       # ≈ -0.8414709848078965
print(polinomio_taylor_seno(3.14159, 15)) # ≈ 0.0000026535897933527
