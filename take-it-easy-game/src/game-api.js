import axios from 'axios';

export const getCurrentTile = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/current_tile');
    return response.data.data;
  } catch (e) {
    console.error('There was an error fetching the tile!', e);
  }
};

export const getAIPlacement = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/agent_location');
    return response.data.data;
  } catch (e) {
    console.error('There was an error fetching the action!', e);
  }
};

export const getAIScore = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/agent_score');
    return response.data.data;
  } catch (e) {
    console.error('There was an error fetching the score!', e);
  }
};

export const chooseAiAgent = async (agent) => {
  try {
    await axios.post('http://127.0.0.1:5000/init_game', {
      agent,
    });
  } catch (e) {
    console.error('There was an error fetching the score!', e);
  }
};
