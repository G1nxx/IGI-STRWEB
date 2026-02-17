class EmployeeBase {
    constructor(lastName, initials, phone) {
        this.lastName = lastName;
        this.initials = initials;
        this.phone = phone;
    }

    get last() { return this.lastName; }
    get init() { return this.initials; }
    get tel() { return this.phone; }

    set tel(v) { this.phone = v; }
}

class EmployeeFull extends EmployeeBase {

    static list = [

        { lastName: "Smith", initials: "J.K.", phone: "+1-555-0101", department: "IT" },
        { lastName: "Johnson", initials: "M.L.", phone: "+1-555-0102", department: "HR" },
        { lastName: "Williams", initials: "R.T.", phone: "+1-555-0103", department: "Finance" },
        { lastName: "Brown", initials: "S.A.", phone: "+1-555-0104", department: "Marketing" },
        { lastName: "Jones", initials: "A.B.", phone: "+1-555-0105", department: "IT" },
        { lastName: "Garcia", initials: "L.M.", phone: "+1-555-0106", department: "Sales" },
        { lastName: "Miller", initials: "D.C.", phone: "+1-555-0107", department: "Operations" },
        { lastName: "Davis", initials: "P.K.", phone: "+1-555-0108", department: "HR" },
        { lastName: "Rodriguez", initials: "F.G.", phone: "+1-555-0109", department: "IT" },
        { lastName: "Martinez", initials: "H.J.", phone: "+1-555-0110", department: "Finance" },
        { lastName: "Wilson", initials: "T.J.", phone: "+1-555-0111", department: "Marketing" },
        { lastName: "Anderson", initials: "K.L.", phone: "+1-555-0112", department: "Sales" },
        { lastName: "Taylor", initials: "W.N.", phone: "+1-555-0113", department: "Operations" },
        { lastName: "Thomas", initials: "E.P.", phone: "+1-555-0114", department: "IT" },
        { lastName: "Jackson", initials: "O.R.", phone: "+1-555-0115", department: "HR" }

    ].map(e => new EmployeeFull(e.lastName, e.initials, e.phone, e.department));

    constructor(lastName, initials, phone, department) {
        super(lastName, initials, phone);
        this.department = department;
    }

    get dep() { return this.department; }
    set dep(v) { this.department = v; }

    static addFromForm() {
        const ln = document.getElementById("add_last").value.trim();
        const init = document.getElementById("add_init").value.trim();
        const phone = document.getElementById("add_phone").value.trim();
        const dep = document.getElementById("add_dep").value.trim();

        if (!ln || !init || !phone || !dep) {
            alert("Fill all fields!");
            return;
        }

        EmployeeFull.list.push(new EmployeeFull(ln, init, phone, dep));
        EmployeeFull.renderList();

        document.getElementById("add_last").value = "";
        document.getElementById("add_init").value = "";
        document.getElementById("add_phone").value = "";
        document.getElementById("add_dep").value = "";
    }

    static renderList() {
        const tbody = document.getElementById("employeesList");

        tbody.innerHTML = EmployeeFull.list
            .map(e => `
                <tr>
                    <td>${e.lastName}</td>
                    <td>${e.initials}</td>
                    <td>${e.phone}</td>
                    <td>${e.department}</td>
                </tr>
        `).join("");
    }

    static search() {
        const ln = document.getElementById("lastName").value.trim();
        const init = document.getElementById("initials").value.trim();
        const resultDiv = document.getElementById("result");

        if (!ln || !init) {
            resultDiv.innerHTML = "Enter both fields!";
            return;
        }

        const emp = EmployeeFull.list.find(e =>
            e.lastName.toLowerCase() === ln.toLowerCase() &&
            e.initials.toLowerCase() === init.toLowerCase()
        );

        if (emp) {
            resultDiv.innerHTML =
                `<b>${emp.lastName} ${emp.initials}</b><br>
                 Phone: ${emp.phone}<br>
                 Department: ${emp.department}`;
        } else {
            resultDiv.innerHTML = "Employee not found";
        }
    }

    static clearForm() {
        document.getElementById("lastName").value = "";
        document.getElementById("initials").value = "";
        document.getElementById("result").innerHTML = "";
    }

    static init() {
        EmployeeFull.renderList();
    }
}

window.onload = () => {
    EmployeeFull.init();
};
