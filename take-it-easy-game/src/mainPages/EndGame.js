import React from 'react';
import {
  Box,
  Button,
  Typography,
  Container,
  Paper,
  Divider,
} from '@mui/material';
import { styled } from '@mui/system';
// import { createTheme, ThemeProvider } from '@mui/material/styles';
// import { lime, purple } from '@mui/material/colors';
import EmojiEventsIcon from '@mui/icons-material/EmojiEvents';
import SentimentVeryDissatisfiedIcon from '@mui/icons-material/SentimentVeryDissatisfied';

// const theme = createTheme({
//   palette: {
//     ochre: {
//       main: '#E3D026',
//       light: '#E9DB5D',
//       dark: '#A29415',
//       contrastText: '#242105',
//     },
//   },
// });

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

const EndGame = ({ playerScore, aiScore, onRestart }) => {
  const isPlayerWinner = playerScore > aiScore;

  return (
    // <ThemeProvider theme={theme}>
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
              {aiScore}
            </Typography>
          </ScoreBox>
        </Box>
        <Box sx={{ textAlign: 'center', mb: 4 }}>
          {isPlayerWinner ? (
            <EmojiEventsIcon sx={{ fontSize: 80, color: '#ffeb3b' }} />
          ) : (
            <SentimentVeryDissatisfiedIcon
              sx={{ fontSize: 80, color: '#f44336' }}
            />
          )}
          <Typography variant="h4" gutterBottom sx={{ fontWeight: '300' }}>
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
            fontWeight: '300',
            borderRadius: '24px',
          }}
        >
          Restart
        </Button>
      </StyledPaper>
    </Container>
    // </ThemeProvider>
  );
};

export default EndGame;
