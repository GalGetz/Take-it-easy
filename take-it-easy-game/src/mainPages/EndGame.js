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
import Board from '../components/Board';

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(4),
  borderRadius: theme.spacing(2),
  textAlign: 'center',
  alignItems: 'center',
  boxShadow: '0 4px 20px rgba(0, 0, 0, 0.1)',
  maxWidth: '800px',
  margin: 'auto',
}));

const ScoreBox = styled(Box)(({ theme }) => ({
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
  padding: theme.spacing(2),
  borderRadius: theme.spacing(1),
  boxShadow: '0 2px 10px rgba(0, 0, 0, 0.2)',
  marginBottom: theme.spacing(2),
}));

const ResultIcon = styled(({ isWinner, ...otherProps }) =>
  isWinner ? (
    <EmojiEventsIcon {...otherProps} />
  ) : (
    <SentimentVeryDissatisfiedIcon {...otherProps} />
  ),
)(({ theme }) => ({
  fontSize: 80,
}));

const EndGame = ({ onRestart, playerTiles, placedAITiles, agent }) => {
  const [score, setScore] = useState(null);
  const [playerScore, setPlayerScore] = useState(null);

  useEffect(() => {
    const fetchScore = async () => {
      const response = await getScores(playerTiles);
      setScore(response.agent_score);
      setPlayerScore(response.user_score);
    };
    fetchScore();
  }, [playerTiles]);

  if (playerScore === null && score === null) {
    return <CircularProgress color="inherit" />;
  }

  const isPlayerWinner = playerScore > score;

  return (
    <Container sx={{ mt: 5, alignItems: 'center' }}>
      <StyledPaper elevation={3}>
        <Typography variant="h2" gutterBottom sx={{ fontWeight: 300 }}>
          Game Over
        </Typography>
        <Divider sx={{ my: 2, borderColor: 'rgba(0, 0, 0, 0.12)' }} />
        <Box sx={{ textAlign: 'left', mb: 4 }}>
          <ScoreBox>
            <Typography variant="h6" sx={{ fontWeight: 300 }}>
              Player Score:
            </Typography>
            <Typography variant="h6" sx={{ fontWeight: 300 }}>
              {playerScore}
            </Typography>
          </ScoreBox>
          <ScoreBox>
            <Typography variant="h6" sx={{ fontWeight: 300 }}>
              AI Score:
            </Typography>
            <Typography variant="h6" sx={{ fontWeight: 300 }}>
              {score}
            </Typography>
          </ScoreBox>
        </Box>
        <Box sx={{ textAlign: 'center', mb: 4 }}>
          <ResultIcon
            isWinner={isPlayerWinner}
            sx={{ color: isPlayerWinner ? '#ffeb3b' : '#f44336' }}
          />
          <Typography variant="h4" gutterBottom sx={{ fontWeight: 300 }}>
            {isPlayerWinner ? 'You Win!' : 'AI Wins!'}
          </Typography>
        </Box>
        <Button
          variant="contained"
          color="primary"
          size="large"
          onClick={onRestart}
          sx={{
            textTransform: 'none',
            fontWeight: 300,
            borderRadius: '24px',
          }}
        >
          Restart
        </Button>
      </StyledPaper>
      <Box
        sx={{
          display: 'flex',
          mt: 4,
          mb: 8,
          ml: 8,
          gap: 5,
        }}
      >
        <Board
          title="Your Board"
          placedTiles={playerTiles}
          loaderTurn
          background={isPlayerWinner}
        />
        <Board
          title={`${agent} Board`}
          placedTiles={placedAITiles}
          loaderTurn
          background={!isPlayerWinner}
        />
      </Box>
    </Container>
  );
};

export default EndGame;
