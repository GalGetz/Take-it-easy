import React, { useState } from 'react';
import ScoreBoard from '../components/ScoreBoard';
import '../styles.css';
import SelectAI from '../components/SelectAI';
import { Box, Button } from '@mui/material';
import Board from '../components/Board';
import TilePicker from '../components/TilePicker';

const tiles = [];
const iValues = [1, 5, 9];
const jValues = [2, 6, 7];
const kValues = [3, 4, 8];

for (const i of iValues) {
  for (const j of jValues) {
    for (const k of kValues) {
      tiles.push([i, j, k]);
    }
  }
}

export function GameFace({ onEndGame }) {
  const [placedTiles, setPlacedTiles] = useState(Array.from({ length: 19 }));
  const [restTiles, setRestTiles] = useState(tiles);
  const [currentTile, setCurrentTile] = useState(() => {
    const randomIndex = Math.floor(Math.random() * restTiles.length);
    const tile = restTiles[randomIndex];
    const tilesArr = Array.from(restTiles);
    tilesArr.splice(randomIndex, 1);
    setRestTiles(tilesArr);

    return tile;
  });

  const pickRandomTile = () => {
    const randomIndex = Math.floor(Math.random() * restTiles.length);
    const tile = restTiles[randomIndex];
    const tilesArr = Array.from(restTiles);
    tilesArr.splice(randomIndex, 1);
    setRestTiles(tilesArr);
    return tile;
  };

  const choosePlace = (index) => {
    const tilesArr = Array.from(placedTiles);
    tilesArr[index] = currentTile;
    setPlacedTiles(tilesArr);
    setCurrentTile(pickRandomTile());
  };

  const endGameRender = () => {
    const playerScore = Math.floor(Math.random() * 100);
    const aiScore = Math.floor(Math.random() * 100); // Placeholder for AI score calculation
    onEndGame(playerScore, aiScore);
    return null;
  };

  const ongoingGameRender = () => (
    <div className="AppContainer">
      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',
          width: '20%',
          justifyContent: 'space-between',
        }}
      >
        <SelectAI />
        <Button variant="contained">Start Game</Button>
      </Box>
      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',
          width: '50%',
          justifyContent: 'space-between',
          marginTop: '30px',
          marginRight: '250px',
        }}
      >
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            height: '100%',
            gap: '30px',
          }}
        >
          <ScoreBoard />
          <TilePicker currentTile={currentTile} />
        </Box>
        <Board
          onChoose={choosePlace}
          currentTile={currentTile}
          placedTiles={placedTiles}
        />
      </Box>
    </div>
  );

  return placedTiles.some((element) => element === undefined)
    ? ongoingGameRender()
    : endGameRender();
}
