import React, { useEffect, useState } from 'react';
import {
  Box,
  Button,
  Typography,
  Container,
  Paper,
  Divider,
  CircularProgress,
} from '@mui/material';
import { getScores } from '../game-api';
import { styled } from '@mui/system';
import EmojiEventsIcon from '@mui/icons-material/EmojiEvents';
import SentimentVeryDissatisfiedIcon from '@mui/icons-material/SentimentVeryDissatisfied';

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(4),
  borderRadius: theme.spacing(2),
  textAlign: 'center',
  boxShadow: '0 4px 20px rgba(0, 0, 0, 0.1)',
}));

const ScoreBox = styled(Box)(({ theme }) => ({
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
  padding: theme.spacing(2),
  borderRadius: theme.spacing(1),
  boxShadow: '0 2px 10px rgba(0, 0, 0, 0.2)',
}));

const EndGame = ({ onRestart, playerTiles }) => {
  const [score, setScore] = useState(null);
  const [playerScore, setPlayerScore] = useState(null);

  useEffect(() => {
    async function fetchScore() {
      console.log(playerTiles);
      const response = await getScores(playerTiles);
      console.log(response);
      setScore(response.agent_score);
      setPlayerScore(response.user_score);
    }
    fetchScore();
  }, []);

  return playerScore ? (
    <Container maxWidth="sm" sx={{ mt: 5 }}>
      <StyledPaper elevation={3}>
        <Box sx={{ mb: 4 }}>
          <Typography variant="h2" gutterBottom sx={{ fontWeight: '300' }}>
            Game Over
          </Typography>
          <Divider sx={{ my: 2, borderColor: 'rgba(0, 0, 0, 0.12)' }} />
        </Box>
        <Box sx={{ textAlign: 'left', mb: 4 }}>
          <ScoreBox sx={{ mb: 2 }}>
            <Typography variant="h6" sx={{ fontWeight: '300' }}>
              Player Score:
            </Typography>
            <Typography variant="h6" sx={{ fontWeight: '300' }}>
              {playerScore}
            </Typography>
          </ScoreBox>
          <ScoreBox sx={{ mb: 2 }}>
            <Typography variant="h6" sx={{ fontWeight: '300' }}>
              AI Score:
            </Typography>
            <Typography variant="h6" sx={{ fontWeight: '300' }}>
              {score}
            </Typography>
          </ScoreBox>
        </Box>
        <Box sx={{ textAlign: 'center', mb: 4 }}>
          {playerScore > score ? (
            <EmojiEventsIcon sx={{ fontSize: 80, color: '#ffeb3b' }} />
          ) : (
            <SentimentVeryDissatisfiedIcon
              sx={{ fontSize: 80, color: '#f44336' }}
            />
          )}
          <Typography variant="h4" gutterBottom sx={{ fontWeight: '300' }}>
            {playerScore > score ? 'You Win!' : 'AI Wins!'}
          </Typography>
        </Box>
        <Button
          variant="contained"
          color="primary"
          size="large"
          onClick={onRestart}
          sx={{
            textTransform: 'none',
            fontWeight: '300',
            borderRadius: '24px',
          }}
        >
          Restart
        </Button>
      </StyledPaper>
    </Container>
  ) : (
    <CircularProgress color="inherit" />
  );
};

export default EndGame;
