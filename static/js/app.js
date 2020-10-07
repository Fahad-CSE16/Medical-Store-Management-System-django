new Vue({
  el: "#app",
  data: {
    t: "Fahad",
    src: "img.jpg",
    alt: "dog",
    link: "https://desirebd.herokupp.com",
    list: ["fahad", "fahmida"],
    age: 18,
    range: 21,
    object: {
      name: "fahad",
      age: 25,
      no: 10,
    },
    functions: () => {
      return "Hello World!";
    },
  },
  methods: {
    namef: function () {
      return this.t;
    },
    namef1() {
      return this.list;
    },
    f() {
      return this.t == "Fahad" ? true : false;
    },
  },
});
var app2 = new Vue({
  el: "#app2",
  data: {
    name: "fahad",
  },
});
var app3 = new Vue({
  el: "#data",
  data: {
    x: 0,
    y: 0,
  },
  methods: {
    getcoord(event) {
      this.x = event.clientX;
      this.y = event.clientY;
    },
  },
});
