// src/App.js
import React, { useState } from 'react';
import { AppBar, Toolbar, Typography } from '@mui/material';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate,
} from 'react-router-dom';
import HomePage from './HomePage';
import EndGame from './EndGame';
import { GameFace } from './GameFace';
import { lime } from '@mui/material/colors';
import '../styles.css';
// import axios from 'axios';

// const API_URL = 'http://127.0.0.1:5000';

function App() {
  const [playerScore, setPlayerScore] = useState(0);
  const [aiScore, setAiScore] = useState(0);

  const navigate = useNavigate();

  const startGame = () => {
    navigate('/game');
  };

  const endGame = (playerScore, aiScore) => {
    setPlayerScore(playerScore);
    setAiScore(aiScore);
    navigate('/end');
  };

  const restartGame = () => {
    navigate('/');
  };

  return (
    <>
      <AppBar position="static" sx={{ borderRadius: 2 }} color="primary">
        <Toolbar>
          <Typography
            variant="h4"
            sx={{
              flexGrow: 1,
              textAlign: 'center',
              fontWeight: 'bold',
              color: '#fff',
            }}
          >
            Take It Easy!
          </Typography>
        </Toolbar>
      </AppBar>
      <Routes>
        <Route path="/" element={<HomePage onStart={startGame} />} />
        <Route path="/game" element={<GameFace onEndGame={endGame} />} />
        <Route
          path="/end"
          element={
            <EndGame
              playerScore={playerScore}
              aiScore={aiScore}
              onRestart={restartGame}
            />
          }
        />
      </Routes>
    </>
  );
}

export default function AppWrapper() {
  return (
    <Router>
      <App />
    </Router>
  );
}
