import React, { useState, useEffect } from 'react';
import styles from './styles/Controls.module.css';

type ControlsProps = {
  balance: number,
  gameState: number,
  buttonState: any,
  betEvent: any,
  hitEvent: any,
  standEvent: any,
  resetEvent: any
};

const Controls: React.FC<ControlsProps> = ({ balance, gameState, buttonState, betEvent, hitEvent, standEvent, resetEvent }) => {
  const [currentBet, setCurrentBet] = useState(0);

  const handleAddToBet = (amount: number) => {
    // if (currentBet + amount <= balance) {
    //   setCurrentBet(currentBet + amount);
    // }
    // else {
    //   alert('Not emough balance for this bet!');
    // }
    setCurrentBet(currentBet + amount);
  };

  const handlePlaceBet = () => {
    // if (currentBet > 0) {
    //   betEvent(currentBet);
    //   setCurrentBet(0);
    // }
    // else {
    //   alert('Please select a valid bet!');
    // }
    betEvent(currentBet);
    setCurrentBet(0);
  };

  const handleAllIn = (amount: number) => {
    setCurrentBet(amount);
  }

  const handleCancelBet = () => {
    setCurrentBet(0);
  };

  const isPlaceBetDisabled = currentBet > balance || currentBet === 0;

  const getBetControls  = () => (
    <div className={styles.controlsContainer}>
      <div className={styles.chipsContainer}>
        <button onClick={() => handleAddToBet(1)} className={styles.chipButton}>1</button>
        <button onClick={() => handleAddToBet(5)} className={styles.chipButton}>5</button>
        <button onClick={() => handleAddToBet(10)} className={styles.chipButton}>10</button>
        <button onClick={() => handleAddToBet(50)} className={styles.chipButton}>50</button>
        <button onClick={() => handleAddToBet(100)} className={styles.chipButton}>100</button>
        <button onClick={() => handleAllIn(balance)} className={styles.chipButton}>All in</button>
      </div>

      <div className={styles.placeBet}>
        <button
          onClick={handleCancelBet}
          className={styles.button}
          disabled={currentBet === 0}
        >
          Reset Bet
        </button>

        <h4 className={styles.placeBetText} style={{ color: currentBet > balance ? 'red' : 'white'}}>${currentBet}</h4>

        <button
          onClick={handlePlaceBet}
          className={styles.button}
          disabled={isPlaceBetDisabled}
          >
            Place Bet
        </button>
      </div>
    </div>
  );

  const getGameControls = () => (
    <div className={styles.controlsContainer}>
      <button onClick={hitEvent} disabled={buttonState.hitDisabled} className={styles.button}>Hit</button>
      <button onClick={standEvent} disabled={buttonState.standDisabled} className={styles.button}>Stand</button>
      <button onClick={resetEvent} disabled={buttonState.resetDisabled} className={styles.button}>Reset</button>
    </div>
  );

  return (
    <>
      {gameState === 0 ? getBetControls() : getGameControls()}
    </>
  );
};

export default Controls;














//   const [amount, setAmount] = useState(10);
//   const [inputStyle, setInputStyle] = useState(styles.input);

//   useEffect(() => {
//     validation();
//   }, [amount, balance]);

//   const validation = () => {
//     if (amount > balance) {
//       setInputStyle(styles.inputError);
//       return false;
//     }
//     if (amount < 0.01) {
//       setInputStyle(styles.inputError);
//       return false;
//     }
//     setInputStyle(styles.input);
//     return true;
//   }

//   const amountChange = (e: any) => {
//     setAmount(e.target.value);
//   }

//   const onBetClick = () => {
//     if (validation()) {
//       betEvent(Math.round(amount * 100) / 100);
//     }
//   }

//   const getControls = () => {
//     if (gameState === 0) {
//       return (
//         <div className={styles.controlsContainer}>
//           <div className={styles.betContainer}>
//             <h4>Amount:</h4>
//             <input autoFocus type='number' value={amount} onChange={amountChange} className={inputStyle} />
//           </div>
//           <button onClick={() => onBetClick()} className={styles.button}>Bet</button>
//         </div>
//       );
//     }
//     else {
//       return (
//         <div className={styles.controlsContainer}>
//           <button onClick={() => hitEvent()} disabled={buttonState.hitDisabled} className={styles.button}>Hit</button>
//           <button onClick={() => standEvent()} disabled={buttonState.standDisabled} className={styles.button}>Stand</button>
//           <button onClick={() => resetEvent()} disabled={buttonState.resetDisabled} className={styles.button}>Reset</button>
//         </div>
//       );
//     }
//   }

//   return (
//     <>
//       {getControls()}
//     </>
//   );
// }