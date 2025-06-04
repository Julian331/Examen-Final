fun factorial(n: Int): Long {
    var resultado = 1L
    for (i in 2..n) {
        resultado *= i
    }
    return resultado
}

fun polinomioTaylorSeno(x: Double, n: Int): Double {
    var senoAprox = 0.0
    var potencia = x          // x^(2k+1), comienza en x^1
    var factorial = 1.0       // (2k+1)!, comienza en 1!
    var signo = 1.0           // (-1)^k

    for (k in 0 until n) {
        val termino = signo * potencia / factorial
        senoAprox += termino

        // Preparar siguiente término
        signo *= -1
        potencia *= x * x
        factorial *= (2 * k + 2) * (2 * k + 3)
    }

    return senoAprox
}
fun main() {
    println(polinomioTaylorSeno(0.0, 5))         // 0.0
    println(polinomioTaylorSeno(1.0, 10))        // ≈ 0.8414709848078965
    println(polinomioTaylorSeno(-1.0, 7))        // ≈ -0.8414709848078965
    println(polinomioTaylorSeno(3.14159, 15))    // ≈ 0.0000026535...
}
