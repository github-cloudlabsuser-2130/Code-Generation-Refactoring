function calculadora(operacion, num1, num2) {
    switch (operacion) {
        case 'suma':
            return num1 + num2;
        case 'resta':
            return num1 - num2;
        case 'multiplicacion':
            return num1 * num2;
        case 'division':
            return num2 !== 0 ? num1 / num2 : 'Error: División por cero';
        default:
            return 'Operación no válida';
    }
}

// Ejemplo de uso:
// console.log(calculadora('suma', 5, 3)); // Salida: 8
// console.log(calculadora('division', 10, 0)); // Salida: Error: División por cero
