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
import { GameFace } from './GamePage';
import '../styles.css';

// const API_URL = 'http://127.0.0.1:5000';
const TILES_SUM = 19;

function App() {
  const navigate = useNavigate();
  const [placedTiles, setPlacedTiles] = useState(
    Array.from({ length: TILES_SUM }),
  );
  const [placedAITiles, setPlacedAITiles] = useState(
    Array.from({ length: TILES_SUM }),
  );
  const [agent, setAgent] = useState('');

  const startGame = () => {
    navigate('/game');
  };

  const endGame = () => {
    navigate('/end');
  };

  const restartGame = () => {
    setPlacedTiles(Array.from({ length: TILES_SUM }));
    setPlacedAITiles(Array.from({ length: TILES_SUM }));
    setAgent('');
    navigate('/');
  };

  return (
    <>
      <AppBar position="static" sx={{ borderRadius: 2 }} color="primary">
        <Toolbar>
          <Typography
            variant="h3"
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
        <Route
          path="/game"
          element={
            <GameFace
              onEndGame={endGame}
              placedTiles={placedTiles}
              setPlacedTiles={setPlacedTiles}
              placedAITiles={placedAITiles}
              setPlacedAITiles={setPlacedAITiles}
              agent={agent}
              setAgent={setAgent}
            />
          }
        />
        <Route
          path="/end"
          element={
            <EndGame
              onRestart={restartGame}
              playerTiles={placedTiles}
              placedAITiles={placedAITiles}
              agent={agent}
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
