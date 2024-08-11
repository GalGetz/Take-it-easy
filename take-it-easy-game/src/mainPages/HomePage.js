import React from 'react';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import { Container, Paper } from '@mui/material';
import LaptopMacIcon from '@mui/icons-material/LaptopMac';
import RepeatIcon from '@mui/icons-material/Repeat';
import {
  Timeline,
  TimelineContent,
  TimelineDot,
  TimelineSeparator,
  TimelineItem,
  TimelineConnector,
} from '@mui/lab';

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

function HomePage({ onStart }) {
  const timeLineOfGame = () => (
    <>
      <Typography variant="h4" component="span">
        TimeLine of the game
      </Typography>
      <Timeline position="alternate">
        <TimelineItem>
          <TimelineSeparator>
            <TimelineConnector />
            <TimelineDot color="primary" variant="outlined" />
            <TimelineConnector />
          </TimelineSeparator>
          <TimelineContent sx={{ py: '12px', px: 2 }}>
            <Typography variant="h6" component="span">
              Choose AI Player
            </Typography>
          </TimelineContent>
        </TimelineItem>
        <TimelineItem>
          <TimelineSeparator>
            <TimelineConnector />
            <TimelineDot color="primary">
              <LaptopMacIcon />
            </TimelineDot>
            <TimelineConnector />
          </TimelineSeparator>
          <TimelineContent sx={{ py: '12px', px: 2 }}>
            <Typography variant="h6" component="span">
              Start to play
            </Typography>
          </TimelineContent>
        </TimelineItem>
        <TimelineItem>
          <TimelineSeparator>
            <TimelineConnector />
            <TimelineDot color="primary" variant="outlined" />
            <TimelineConnector />
          </TimelineSeparator>
          <TimelineContent sx={{ py: '12px', px: 2 }}>
            <Typography variant="h6" component="span">
              Score Board
            </Typography>
          </TimelineContent>
        </TimelineItem>
        <TimelineItem>
          <TimelineSeparator>
            <TimelineConnector />
            <TimelineDot color="secondary">
              <RepeatIcon />
            </TimelineDot>
            <TimelineConnector />
          </TimelineSeparator>
          <TimelineContent sx={{ py: '12px', px: 2 }}>
            <Typography variant="h6" component="span">
              Repeat
            </Typography>
          </TimelineContent>
        </TimelineItem>
      </Timeline>
      <Box sx={{ mt: 4 }}>
        <Button
          variant="contained"
          color="primary"
          size="large"
          onClick={onStart}
        >
          Let's play
        </Button>
      </Box>
    </>
  );

  const instructionsCard = () => {
    return (
      <Box sx={{ textAlign: 'left' }}>
        <Typography variant="h4" gutterBottom>
          Instructions
        </Typography>
        <Typography variant="h6" gutterBottom>
          The Start
        </Typography>
        <Typography variant="body2" paragraph>
          Start with an empty board. Place the hexagonal pieces to form
          continuous lines of one color from one edge to another. Collect points
          over four rounds, and the highest score wins.
        </Typography>
        <Typography variant="h6" gutterBottom>
          First Round
        </Typography>
        <Typography variant="body2" paragraph>
          The caller shuffles their pieces face down, while other players keep
          theirs face up and grouped by top number.
        </Typography>
        <Typography variant="h6" gutterBottom>
          The Game
        </Typography>
        <Typography variant="body2" paragraph>
          The caller picks a piece, announces its values, and places it on the
          board. Other players place their matching pieces on their boards
          simultaneously. Continue until all spaces are filled.
        </Typography>
        <Typography variant="h6" gutterBottom>
          Placing Pieces
        </Typography>
        <Typography variant="body2" paragraph>
          Place pieces vertically with numbers upright. Once placed, pieces
          cannot be moved, but you can adjust them until the next tile is
          announced. Strategize to avoid breaking high-value lines.
        </Typography>
        <Typography variant="h6" gutterBottom>
          Scoring
        </Typography>
        <Typography variant="body2" paragraph>
          After all pieces are placed, score each complete line of the same
          color from edge to edge. Lines can be vertical, or diagonal in either
          direction. Calculate points as the length of the line times the value
          of the color.
        </Typography>
      </Box>
    );
  };

  return (
    <Container sx={{ mt: 5 }}>
      <PaperWrapper noMt>
        <Typography variant="h2" gutterBottom>
          Welcome to Take It Easy!
        </Typography>
        <Typography variant="body1" paragraph>
          Take It Easy is a simple yet addictive puzzle game. Arrange tiles on
          the board to score as many points as possible. Follow the instructions
          below to get started.
        </Typography>
      </PaperWrapper>
      <PaperWrapper>{instructionsCard()}</PaperWrapper>
      <PaperWrapper>{timeLineOfGame()}</PaperWrapper>
    </Container>
  );
}

export default HomePage;
