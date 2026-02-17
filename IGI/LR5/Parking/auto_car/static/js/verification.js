function calcAge(dateStr) {
    const [y, m, d] = dateStr.split("-").map(Number);
    const birth = new Date(y, m - 1, d);
    const today = new Date();

    let age = today.getFullYear() - birth.getFullYear();
    const monthDiff = today.getMonth() - birth.getMonth();

    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birth.getDate())) {
        age--;
    }
    return age;
}

function isValidDate(dateStr) {
    const regex = /^\d{4}-\d{2}-\d{2}$/;
    if (!regex.test(dateStr)) return false;

    const [y, m, d] = dateStr.split("-").map(Number);

    const date = new Date(y, m - 1, d);
    if (
        date.getFullYear() !== y ||
        date.getMonth() !== m - 1 ||
        date.getDate() !== d
    ) return false;

    const today = new Date();
    if (date > today) return false;

    if (today.getFullYear() - y > 120) return false;

    return true;
}

function getWeekDay(dateStr) {
    const [y, m, d] = dateStr.split("-").map(Number);
    const date = new Date(y, m - 1, d);
    const days = ["воскресенье", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота"];
    return days[date.getDay()];
}

function getYear(dateStr) {
    const [y, m, d] = dateStr.split("-").map(Number);
    const target = new Date(y, m - 1, d);
    const now = new Date();

    let years = now.getFullYear() - target.getFullYear();

    const hasHadBirthday =
        now.getMonth() > target.getMonth() ||
        (now.getMonth() === target.getMonth() && now.getDate() >= target.getDate());

    if (!hasHadBirthday) years--;

    return years;
}


document.addEventListener("DOMContentLoaded", () => {
    const banner = document.querySelector(".banner");
    let dob = null;

    while (true) {
        dob = prompt("Введите вашу дату рождения (в формате ГГГГ-ММ-ДД):");
        
        if (dob === null) {
            alert("Дата рождения необходима для продолжения.");
            continue;
        }

        if (!isValidDate(dob)) {
            alert("Дата введена неверно! Используйте формат ГГГГ-ММ-ДД.");
            continue;
        }

        const age = calcAge(dob);

        if (age < 18) {
            alert("Вам меньше 18 лет. Использование сайта возможно только с разрешения родителей.");
            continue;
        }

        break;
    }

    alert(`Вам ${getYear(dob)} лет\nВы родились в ${getWeekDay(dob)}.`);

    const btn = document.createElement("button");
    btn.textContent = "Перейти на страницу";
    btn.style.marginTop = "10px";
    btn.style.padding = "10px 15px";
    btn.style.cursor = "pointer";
    btn.style.display = "block";

    banner.appendChild(btn);

    btn.addEventListener("click", () => {
        window.location.href = "/about/";
    });
});
