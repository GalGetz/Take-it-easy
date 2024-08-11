import axios from 'axios';

export const getCurrentTile = async () => {
  try {
    const response = await axios.get('http://localhost:5000/api/current_tile');
    return response.data;
  } catch (e) {
    console.error('There was an error fetching the tile!', e);
  }
};

export const getAIPlacement = async () => {
  try {
    const response = await axios.get(
      'http://localhost:5000/api/agent_loaction',
    );
    return response.data;
  } catch (e) {
    console.error('There was an error fetching the action!', e);
  }
};

export const getAIScore = async () => {
  try {
    const response = await axios.get('http://localhost:5000/api/score');
    return response.data;
  } catch (e) {
    console.error('There was an error fetching the score!', e);
  }
};

export const chooseAiAgent = async (agent) => {
  try {
    await axios.post('http://localhost:5000/api/agent', {
      agent: agent,
    });
  } catch (e) {
    console.error('There was an error fetching the score!', e);
  }
};
