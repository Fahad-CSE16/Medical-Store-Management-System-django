var d = new Vue({
  el: "#app",
  data: {
    cart: [],
  },
  computed: {},
  methods: {
    addCartItem(i) {
      this.cart.push(i);
      console.log(cart);
    },
  },
});
