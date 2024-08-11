import React, { useState, useEffect } from 'react';
// import ScoreBoard from '../components/ScoreBoard';
import '../styles.css';
import { getAIPlacement, getCurrentTile } from '../game-api';
import SelectAI from '../components/SelectAI';
import { Box, Button } from '@mui/material';
import Board from '../components/Board';
import TilePicker from '../components/TilePicker';

// const tiles = [];
// const iValues = [1, 5, 9];
// const jValues = [2, 6, 7];
// const kValues = [3, 4, 8];

// for (const i of iValues) {
//   for (const j of jValues) {
//     for (const k of kValues) {
//       tiles.push([i, j, k]);
//     }
//   }
// }

export function GameFace({ onEndGame }) {
  const [placedTiles, setPlacedTiles] = useState(Array.from({ length: 19 }));
  const [placedAITiles, setPlacedAITiles] = useState(
    Array.from({ length: 19 }),
  );
  // const [restTiles, setRestTiles] = useState(tiles);
  const [agent, setAgent] = React.useState('');
  const [currentTile, setCurrentTile] = useState(null);

  // const pickRandomTile = () => {
  //   const randomIndex = Math.floor(Math.random() * restTiles.length);
  //   const tile = restTiles[randomIndex];
  //   const tilesArr = Array.from(restTiles);
  //   tilesArr.splice(randomIndex, 1);
  //   setRestTiles(tilesArr);
  //   return tile;
  // };

  useEffect(async () => {
    const current = getCurrentTile();
    setCurrentTile(current);
  }, []);

  const choosePlace = async (index) => {
    const tilesArr = Array.from(placedTiles);
    tilesArr[index] = currentTile;
    setPlacedTiles(tilesArr);

    const AItilesArr = Array.from(placedAITiles);
    const AIindex = await getAIPlacement();
    AItilesArr[AIindex] = currentTile;
    setPlacedAITiles(AItilesArr);

    const current = await getCurrentTile();
    setCurrentTile(current);
  };

  const endGameRender = () => {
    onEndGame();
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
        <SelectAI agent={agent} setAgent={setAgent} />
        <Button variant="contained">Start Game</Button>
      </Box>
      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',
          width: '70%',
          justifyContent: 'space-between',
          marginTop: '30px',
          marginRight: '150px',
          gap: '20px',
        }}
      >
        <Board
          title={'Your Board'}
          onChoose={choosePlace}
          placedTiles={placedTiles}
        />
        <Box>
          <TilePicker currentTile={currentTile} />
        </Box>
        <Board
          title={`${agent} Board`}
          onChoose={() => {}}
          placedTiles={placedAITiles}
        />
      </Box>
    </div>
  );

  return placedTiles.some((element) => element === undefined)
    ? ongoingGameRender()
    : endGameRender();
}
