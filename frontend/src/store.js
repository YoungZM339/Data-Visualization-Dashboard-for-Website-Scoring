import Vue from 'vue';
import Vuex from 'vuex';
import api from './api.js';

Vue.use(Vuex);

const store = new Vuex.Store({
        state: {
            processed_data: null
        },
        getters: {
            calculated_data: state => {
                if (!state.processed_data) {
                    return {};
                }
                let stats = {};
                state.processed_data.forEach(item => {
                    for (let key in item) {
                        if (item[key] !== null) {
                            if (!stats[key]) {
                                stats[key] = {
                                    total: 0,
                                    count: 0
                                };
                            }

                            stats[key].total += parseInt(item[key]);
                            stats[key].count++;
                        }
                    }
                });

                let result = {};

                for (let key in stats) {
                    result[key] = {
                        total: stats[key].total,
                        average: stats[key].total / stats[key].count
                    };
                }

                return result;
            },
            char_array: state => {
                let num;
                num = Object.keys(state.processed_data).length;
                return num.toString().split('');
            },
            event_name_array: state => {
                let eventCounter = {};
                state.processed_data.forEach(item => {
                    if (eventCounter[item.eventName]) {
                        eventCounter[item.eventName] += 1;
                    } else {
                        eventCounter[item.eventName] = 1;
                    }
                });
                return eventCounter;
            }
        },
        mutations: {
            set_processed_data: (state, data) => {
                state.processed_data = data;
            }
        },
        actions: {
            fetch_data: async ({commit}) => {
                try {
                    const response = await api.get('/algorithms/get-processed-data/');
                    const data = response.data;
                    commit('set_processed_data', data);
                    return data;
                } catch (error) {
                    console.log(error);
                    if (error.response && error.response.status === 401) {
                        console.log('Data fetch error:', "Unauthorized");
                    } else {
                        console.log('Data fetch error:', error.message);
                    }
                    throw error;
                }
            }

        }
    })
;

export default store;
