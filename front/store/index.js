import Vuex from 'vuex';

const store = {
  state: {
    notes: {},
    users: {},
    userItems: {}
  },
  getters: {
    items: state => state.items,
    users: state => state.users,
    userItems: state => state.userItems
  },
  mutations: {
    setItems(state, { items }) {
      state.items = items;
    },
    setUser(state, { user }) {
      state.users[user.id] = user;
    },
    setUserItems(state, { user, items }) {
      state.userItems[user.id] = items;
    }
  },
  actions: {
    async fetchNote({ commit }, { params }) {
      console.log("username:"+params.user+", notetitle:"+params.note)
      const note = await this.$axios.$get(
        `http://wisnote-api:5000/api/${params.user}/${params.note}`
      );
      commit('setNote', { note });
    }
  }
};

export default () => new Vuex.Store(store);
