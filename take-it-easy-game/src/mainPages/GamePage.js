import React, { useState, useEffect } from 'react';
// import ScoreBoard from '../components/ScoreBoard';
import '../styles.css';
import { getAIPlacement, getCurrentTile } from '../game-api';
import SelectAI from '../components/SelectAgent/SelectAI';
import { Box, Button } from '@mui/material';
import Board from '../components/Board';
import TilePicker from '../components/TilePicker';
import ContentAi from '../components/SelectAgent/ContentAi';

const TILES_SUM = 19;

export function GameFace({ onEndGame }) {
  const [placedTiles, setPlacedTiles] = useState(
    Array.from({ length: TILES_SUM }),
  );
  const [placedAITiles, setPlacedAITiles] = useState(
    Array.from({ length: TILES_SUM }),
  );
  const [agent, setAgent] = useState('');
  const [currentTile, setCurrentTile] = useState(null);
  const [isGameStarted, setIsGameStarted] = useState(false);

  useEffect(() => {
    async function fetchData() {
      const current = await getCurrentTile();
      console.log(current);
      setCurrentTile(current);
    }
    fetchData();
  }, []);

  const choosePlace = async (index) => {
    const tilesArr = Array.from(placedTiles);
    tilesArr[index] = currentTile;
    setPlacedTiles(tilesArr);

    const AItilesArr = Array.from(placedAITiles);
    const AIindex = await getAIPlacement();
    console.log(AIindex);
    AItilesArr[AIindex] = currentTile;
    setPlacedAITiles(AItilesArr);

    const current = await getCurrentTile();
    console.log(current);
    setCurrentTile(current);
  };

  const endGameRender = () => {
    onEndGame();
    return null;
  };

  const agentChooseRender = () => {
    return (
      <>
        <Box
          sx={{
            display: 'flex',
            alignItems: 'center',
            width: '25%',
            justifyContent: 'space-between',
          }}
        >
          <SelectAI agent={agent} setAgent={setAgent} />
          <Button
            variant="contained"
            onClick={() => setIsGameStarted(true)}
            disabled={!agent}
          >
            Start Game
          </Button>
        </Box>
        {agent && <ContentAi agent={agent} />}
      </>
    );
  };
  const ongoingGameRender = () => (
    <div className="AppContainer">
      {isGameStarted ? (
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
      ) : (
        agentChooseRender()
      )}
    </div>
  );

  return placedTiles.some((element) => element === undefined)
    ? ongoingGameRender()
    : endGameRender();
}
