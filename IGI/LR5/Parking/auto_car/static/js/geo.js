
function getLocation() {
    const result = document.getElementById('result');
    
    if (!navigator.geolocation) {
        result.innerHTML = 'Геолокация не поддерживается';
        return;
    }
    
    result.innerHTML = 'Определяем местоположение...';
    
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const lat = position.coords.latitude;
            const lng = position.coords.longitude;
            
            result.innerHTML = `
                <h3>Ваше местоположение:</h3>
                <p>Широта: ${lat.toFixed(6)}</p>
                <p>Долгота: ${lng.toFixed(6)}</p>
                <p>Точность: ±${position.coords.accuracy} метров</p>
                <a href="https://maps.google.com/?q=${lat},${lng}" target="_blank">
                    Показать на Google Maps
                </a>
            `;
        },
        function(error) {
            let message = 'Ошибка: ';
            switch(error.code) {
                case 1: message += 'Доступ запрещен'; break;
                case 2: message += 'Местоположение недоступно'; break;
                case 3: message += 'Время ожидания истекло'; break;
            }
            result.innerHTML = message;
        },
        {
            enableHighAccuracy: true,
            timeout: 10000,
            maximumAge: 60000
        }
    );
}