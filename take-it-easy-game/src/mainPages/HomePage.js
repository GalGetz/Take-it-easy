import React, { useState } from 'react';
import {
  Typography,
  Button,
  Box,
  Container,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Grid,
  Card,
  CardContent,
} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
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

const HomePage = ({ onStart }) => {
  const [expanded, setExpanded] = useState(false);

  const handleAccordionChange = (panel) => (event, isExpanded) => {
    setExpanded(isExpanded ? panel : false);
  };

  const timeLineOfGame = () => (
    <Card elevation={3} sx={{ padding: 4, borderRadius: 3, minHeight: 520 }}>
      <CardContent>
        <Typography variant="h4" sx={{ mb: 6 }} align="center">
          Timeline of the Game
        </Typography>
        <Timeline position="alternate">
          <TimelineItem>
            <TimelineSeparator>
              <TimelineConnector />
              <TimelineDot color="primary" variant="outlined" />
              <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent sx={{ py: '18px', px: 2 }}>
              <Typography variant="h6">Choose AI Player</Typography>
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
            <TimelineContent sx={{ py: '18px', px: 2 }}>
              <Typography variant="h6">Start to Play</Typography>
            </TimelineContent>
          </TimelineItem>
          <TimelineItem>
            <TimelineSeparator>
              <TimelineConnector />
              <TimelineDot color="primary" variant="outlined" />
              <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent sx={{ py: '18px', px: 2 }}>
              <Typography variant="h6">Score Board</Typography>
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
            <TimelineContent sx={{ py: '18px', px: 2 }}>
              <Typography variant="h6">Repeat</Typography>
            </TimelineContent>
          </TimelineItem>
        </Timeline>
        <Box sx={{ mt: 6, textAlign: 'center' }}>
          <Button
            variant="contained"
            color="primary"
            size="large"
            onClick={onStart}
            sx={{ borderRadius: 3 }}
          >
            Let's Play
          </Button>
        </Box>
      </CardContent>
    </Card>
  );

  const instructionsCard = () => (
    <Card elevation={3} sx={{ padding: 4, borderRadius: 3, minHeight: 520 }}>
      <CardContent>
        <Typography variant="h4" gutterBottom align="center">
          Instructions
        </Typography>
        <Accordion
          expanded={expanded === 'panel1'}
          onChange={handleAccordionChange('panel1')}
        >
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography variant="h6">The Start</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography variant="body2">
              Start with an empty board. Place the hexagonal pieces to form
              continuous lines of one color from one edge to another. the
              highest score wins.
            </Typography>
          </AccordionDetails>
        </Accordion>
        <Accordion
          expanded={expanded === 'panel2'}
          onChange={handleAccordionChange('panel2')}
        >
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography variant="h6">First Round</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography variant="body2">
              The current tile will be displayed in the center of the page.
              Place it carefully, as you won’t be able to change it afterward.
              Once you've placed the tile, the AI player will make its move.
            </Typography>
          </AccordionDetails>
        </Accordion>
        <Accordion
          expanded={expanded === 'panel3'}
          onChange={handleAccordionChange('panel3')}
        >
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography variant="h6">The Game</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography variant="body2">
              The remainder of the game will proceed just like the first round.
              Keep going until all spaces are filled.
            </Typography>
          </AccordionDetails>
        </Accordion>
        <Accordion
          expanded={expanded === 'panel4'}
          onChange={handleAccordionChange('panel4')}
        >
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography variant="h6">Placing Pieces</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography variant="body2">
              Place pieces vertically with numbers upright. Once placed, pieces
              cannot be moved.
            </Typography>
          </AccordionDetails>
        </Accordion>
        <Accordion
          expanded={expanded === 'panel5'}
          onChange={handleAccordionChange('panel5')}
        >
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography variant="h6">Scoring</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography variant="body2">
              After all pieces are placed, score each complete line of the same
              color from edge to edge. Lines can be vertical, or diagonal in
              either direction. Calculate points as the length of the line times
              the value of the color.
            </Typography>
          </AccordionDetails>
        </Accordion>
      </CardContent>
    </Card>
  );

  return (
    <Container sx={{ mt: 3 }}>
      <Box sx={{ textAlign: 'center', mb: 3 }}>
        <Typography variant="h6" paragraph>
          Take It Easy is a simple yet addictive puzzle game. Arrange tiles on
          the board to score as many points as possible.
        </Typography>
      </Box>
      <Grid container mb={8} spacing={2} justifyContent="center">
        <Grid item xs={12} md={6}>
          {instructionsCard()}
        </Grid>
        <Grid item xs={12} md={6}>
          {timeLineOfGame()}
        </Grid>
      </Grid>
    </Container>
  );
};

export default HomePage;
