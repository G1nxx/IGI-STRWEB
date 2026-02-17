class Slider {
    constructor(root, slides, options = {}) {
        this.root = root;
        this.slides = slides;

        const savedOptions = this.loadOptions();

        this.options = Object.assign({
            loop: true,
            navs: true,
            pags: true,
            auto: false,
            delay: 5,
            stopMouseHover: false
        }, savedOptions, options);

        this.index = 0;
        this.timer = null;

        this.render();
        this.update();
        this.initAuto();
        this.initHoverStop();
        this.initAdminForm();
    }

    render() {
        this.root.innerHTML = "";

        this.slidesContainer = document.createElement("div");
        this.slidesContainer.className = "slider-slides";

        this.slideElems = this.slides.map((s) => {
            const div = document.createElement("div");
            div.className = "slider-slide";

            div.innerHTML = `
                <a href="${s.link}">
                    <img src="${s.img}">
                </a>
                <div class="slider-caption">${s.caption}</div>
            `;

            this.slidesContainer.appendChild(div);
            return div;
        });

        this.root.appendChild(this.slidesContainer);

        this.counterElem = document.createElement("div");
        this.counterElem.className = "slider-counter";
        this.root.appendChild(this.counterElem);

        if (this.options.navs) {
            this.prevBtn = document.createElement("div");
            this.nextBtn = document.createElement("div");

            this.prevBtn.className = "slider-nav prev";
            this.nextBtn.className = "slider-nav next";

            this.prevBtn.textContent = "‹";
            this.nextBtn.textContent = "›";

            this.root.appendChild(this.prevBtn);
            this.root.appendChild(this.nextBtn);

            this.prevBtn.onclick = () => this.prev();
            this.nextBtn.onclick = () => this.next();
        } else {
            this.prevBtn = null;
            this.nextBtn = null;
        }

        if (this.options.pags) {
            this.pags = document.createElement("div");
            this.pags.className = "slider-pagination";

            this.dots = this.slides.map((_, i) => {
                const dot = document.createElement("div");
                dot.className = "slider-dot";
                dot.onclick = () => this.goTo(i);
                this.pags.appendChild(dot);
                return dot;
            });

            this.root.appendChild(this.pags);
        } else {
            this.pags = null;
            this.dots = [];
        }
    }

    update() {
        this.slideElems.forEach((el, i) =>
            el.classList.toggle("active", i === this.index)
        );

        if (this.options.pags && this.dots.length) {
            this.dots.forEach((d, i) =>
                d.classList.toggle("active", i === this.index)
            );
        }

        this.counterElem.textContent = `${this.index + 1}/${this.slides.length}`;
    }

    next() {
        if (this.index < this.slides.length - 1) this.index++;
        else if (this.options.loop) this.index = 0;
        this.update();
    }

    prev() {
        if (this.index > 0) this.index--;
        else if (this.options.loop) this.index = this.slides.length - 1;
        this.update();
    }

    goTo(i) {
        this.index = i;
        this.update();
    }

    initAuto() {
        if (!this.options.auto) return;

        this.timer = setInterval(() => this.next(), this.options.delay * 1000);
    }

    restartAuto() {
        if (!this.options.auto) return;
        clearInterval(this.timer);
        this.initAuto();
    }

    initHoverStop() {
        if (!this.options.auto || !this.options.stopMouseHover) return;

        this.root.addEventListener("mouseenter", () => clearInterval(this.timer));
        this.root.addEventListener("mouseleave", () => this.restartAuto());
    }

    setOptions(newOptions) {
        this.options = { ...this.options, ...newOptions };
        this.saveOptions();

        this.render();
        this.update();

        clearInterval(this.timer);
        this.initAuto();
        this.initHoverStop();
    }

    saveOptions() {
        localStorage.setItem("sliderOptions", JSON.stringify(this.options));
    }

    loadOptions() {
        const saved = localStorage.getItem("sliderOptions");
        if (!saved) return {};
        try {
            return JSON.parse(saved);
        } catch {
            return {};
        }
    }

    initAdminForm() {
        const form = document.getElementById("adminForm");
        if (!form) return;

        document.getElementById("delayInput").value = this.options.delay;
        document.getElementById("loopInput").checked = this.options.loop;
        document.getElementById("navsInput").checked = this.options.navs;
        document.getElementById("pagsInput").checked = this.options.pags;
        document.getElementById("autoInput").checked = this.options.auto;
        document.getElementById("stopMouseHoverInput").checked = this.options.stopMouseHover;

        form.onsubmit = (e) => {
            e.preventDefault();

            const newOptions = {
                delay: parseInt(document.getElementById("delayInput").value) || 5,
                loop: document.getElementById("loopInput").checked,
                navs: document.getElementById("navsInput").checked,
                pags: document.getElementById("pagsInput").checked,
                auto: document.getElementById("autoInput").checked,
                stopMouseHover: document.getElementById("stopMouseHoverInput").checked,
            };

            this.setOptions(newOptions);
        };
    }
}
