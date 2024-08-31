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
      case 'Random':
        return 'The Random option involves making decisions or selections without any specific strategy, relying entirely on chance. It can be useful in scenarios where a baseline or simple comparison is needed against more sophisticated algorithms.';
      case 'Expectimax':
        return 'The Expectimax search algorithm is a game theory algorithm used to maximize the expected utility. It is a variation of the Minimax algorithm. While Minimax assumes that the adversary(the minimizer) plays optimally, the Expectimax doesn’t. This is useful for modelling environments where adversary agents are not optimal, or their actions are based on chance.';
      case 'Reflex':
        return 'A baseline agent - not so good. tries to maximize current board.';
      case 'Monte Carlo':
        return 'The Monte Carlo method is a statistical technique that relies on random sampling to approximate solutions to quantitative problems. It is widely used in various fields, including finance, physics, and optimization, for tasks such as estimating probabilities or simulating systems.';
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
