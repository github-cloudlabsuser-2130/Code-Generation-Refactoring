// https://api.openweathermap.org/data/2.5/weather?q=London&appid=7
// 1. Crear una funcion que se encargue de conectarse a la api y obtener la informacion del clima

const fetchWeather = async (city) => {
    const apiKey = '08a7405286894c6d5fcc338cdb245207'; // Reemplaza con tu API key de OpenWeatherMap
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`Error: ${response.status} - ${response.statusText}`);
        }
        const weatherData = await response.json();
        console.log(`El clima en ${city} es:`, weatherData);
        return weatherData;
    } catch (error) {
        console.error('Hubo un problema al obtener el clima:', error.message);
    }
};

// Ejemplo de uso
fetchWeather('London');