import axios from 'axios';

const API_URL = 'http://localhost:8080';

const produceEventToExploreTopic = () => {
  return axios.post(`${API_URL}/event/explore`);
};

const produceEventToBuyTopic = () => {
  return axios.post(`${API_URL}/event/buy`);
};

export default {
  produceEventToExploreTopic,
  produceEventToBuyTopic,
};