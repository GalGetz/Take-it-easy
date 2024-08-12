// src/components/TilePicker.js
import React from 'react';
import Tile from './Tile';
import '../styles.css';
import Card from '@mui/material/Card';
import { CardContent, CardHeader, CircularProgress } from '@mui/material';

function TilePicker({ currentTile, loaderTurn }) {
  return (
    <Card
      variant="outlined"
      sx={{ textAlign: 'center', justifyContent: 'center' }}
    >
      <CardHeader title="Current Tile" />
      {loaderTurn ? (
        <CircularProgress />
      ) : (
        <CardContent>
          <div style={{ width: 100, height: 80, marginLeft: 10 }}>
            {currentTile && <Tile values={currentTile} isPicker={true} />}
          </div>
        </CardContent>
      )}
    </Card>
  );
}

export default TilePicker;
