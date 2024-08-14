import React, { useState } from 'react';
// import ScoreBoard from '../components/ScoreBoard';
import '../styles.css';
import { getAIPlacement, getCurrentTile, chooseAiAgent } from '../game-api';
import SelectAI from '../components/SelectAgent/SelectAI';
import { Box, Button, CircularProgress } from '@mui/material';
import Board from '../components/Board';
import TilePicker from '../components/TilePicker';
import ContentAi from '../components/SelectAgent/ContentAi';

export function GameFace({
  onEndGame,
  placedTiles,
  setPlacedTiles,
  agent,
  setAgent,
  placedAITiles,
  setPlacedAITiles,
}) {
  const [loaderTurn, setLoaderTurn] = useState(false);
  const [currentTile, setCurrentTile] = useState(null);
  const [isGameStarted, setIsGameStarted] = useState(false);
  const [loading, setLoading] = useState(false);

  const startGame = async () => {
    setLoading(true);
    await chooseAiAgent(agent);
    setIsGameStarted(true);
    const current = await getCurrentTile();
    console.log(current);
    setCurrentTile(current);
    setLoading(false);
  };

  const choosePlace = async (index) => {
    const tilesArr = Array.from(placedTiles);
    tilesArr[index] = currentTile;
    setPlacedTiles(tilesArr);
    //console.log

    const AItilesArr = Array.from(placedAITiles);
    setLoaderTurn(true);
    const AIindex = await getAIPlacement();
    AItilesArr[AIindex] = currentTile;
    setPlacedAITiles(AItilesArr);

    const current = await getCurrentTile();
    setCurrentTile(current);
    setLoaderTurn(false);
  };

  const endGameRender = () => {
    onEndGame();
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
            onClick={() => startGame()}
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
        !loading ? (
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
              loaderTurn={loaderTurn}
            />
            <Box>
              <TilePicker currentTile={currentTile} loaderTurn={loaderTurn} />
            </Box>
            <Board
              title={`${agent} Board`}
              placedTiles={placedAITiles}
              loaderTurn={true}
            />
          </Box>
        ) : (
          <CircularProgress />
        )
      ) : (
        agentChooseRender()
      )}
    </div>
  );

  return placedTiles.some((element) => element === undefined)
    ? ongoingGameRender()
    : endGameRender();
}
