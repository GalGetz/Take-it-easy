import React from 'react';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { Container, Paper } from '@mui/material';

function PaperWrapper({ children, noMt }) {
  return (
    <Paper
      elevation={3}
      sx={{
        padding: 4,
        borderRadius: 2,
        textAlign: 'center',
        mt: noMt ? 0 : 5,
      }}
    >
      {children}
    </Paper>
  );
}

function ContentAi({ agent }) {
  const getContent = () => {
    switch (agent) {
      case 'RL':
        return 'Reinforcement Learning is a type of machine learning where an agent learns to make decisions by interacting with an environment, receiving feedback through rewards or penalties, and optimizing its actions over time to maximize cumulative rewards.';
      case 'Random':
        return 'The Random option involves making decisions or selections without any specific strategy, relying entirely on chance. It can be useful in scenarios where a baseline or simple comparison is needed against more sophisticated algorithms.';
      case 'Monte Carlo':
        return 'The Monte Carlo method is a statistical technique that relies on random sampling to approximate solutions to quantitative problems. It is widely used in various fields, including finance, physics, and optimization, for tasks such as estimating probabilities or simulating systems.';
      case 'A-star':
        return 'A-star (A*) is a popular search algorithm used in pathfinding and graph traversal. It finds the shortest path from a starting point to a goal by using a heuristic to estimate the cost to reach the goal, making it efficient in navigating complex environments.';
      default:
        return '';
    }
  };
  const explanationCard = () => {
    return (
      <Box sx={{ textAlign: 'left' }}>
        <Typography variant="h6" gutterBottom>
          {agent} explanation
        </Typography>
        <Typography variant="body2" paragraph>
          {getContent()}
        </Typography>
      </Box>
    );
  };

  return (
    <Container sx={{ mt: 5, width: '70%' }}>
      <PaperWrapper>{explanationCard()}</PaperWrapper>
    </Container>
  );
}

export default ContentAi;
