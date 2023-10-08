import React, { useEffect, useState, useRef } from 'react';
import styled from 'styled-components';
import html2canvas from 'html2canvas';

const FortuneModal = ({ isOpen, onClose }) => {
  const [fortuneDetail, setFortuneDetail] = useState([]);
  const [randomFortune, setRandomFortune] = useState('');
  const [typingText, setTypingText] = useState('');
  const fortuneRef = useRef(null);

  const handleOverlayClick = e => {
    if (e.target === e.currentTarget) {
      onClose();
    }
  };

  useEffect(() => {
    fetch('/data/fortune_unlogged.json')
      .then(response => response.json())
      .then(result => {
        setFortuneDetail(result);
        const randomIndex = Math.floor(Math.random() * result.length);
        setRandomFortune(result[randomIndex].content);
      });
  }, []);

  const handleCapture = () => {
    html2canvas(fortuneRef.current, { scale: 4 }).then(canvas => {
      const capturedImage = canvas.toDataURL('image/png');
      const link = document.createElement('a');
      link.href = capturedImage;
      link.download = 'fortune_capture.png';
      link.click();
    });
  };

  const handleRedrawFortune = () => {
    const randomIndex = Math.floor(Math.random() * fortuneDetail.length);
    setRandomFortune(fortuneDetail[randomIndex].content);
  };

  const startTypingEffect = text => {
    let currentText = '';
    let index = 0;

    const typingInterval = setInterval(() => {
      if (index < text.length) {
        currentText += text[index];
        setTypingText(currentText);
        index++;
      } else {
        clearInterval(typingInterval);
      }
    }, 90);
  };

  useEffect(() => {
    if (randomFortune) {
      startTypingEffect(randomFortune);
    }
  }, [randomFortune]);

  return isOpen ? (
    <ModalOverlay onClick={handleOverlayClick}>
      <FortuneModalContainer>
        <ModalCloseButton onClick={onClose}>&times;</ModalCloseButton>
        <ModalContent ref={fortuneRef}>
          <DailyVSLogo>Daily VS</DailyVSLogo>
          <img src="/images/Fortune/Fortune_open.png" />
          <FortuneWords>{typingText}</FortuneWords>
        </ModalContent>
        <ModalBtns>
          <AgainBtn onClick={handleRedrawFortune}>다시뽑기</AgainBtn>
          <CaptureBtn onClick={handleCapture}>캡처하기</CaptureBtn>
        </ModalBtns>
      </FortuneModalContainer>
    </ModalOverlay>
  ) : null;
};

export default FortuneModal;

const ModalOverlay = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
`;

const FortuneModalContainer = styled.div`
  background-color: white;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  position: relative;
  width: 400px;
  height: 400px;
`;

const ModalCloseButton = styled.button`
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: transparent;
  border: none;
  font-size: 24px;
  cursor: pointer;
`;

const ModalContent = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  & img {
    margin-top: 15px;
    width: 300px;
  }
`;

const DailyVSLogo = styled.h2`
  margin-top: 10px;
  font-size: 24px;
  font-family: 'GongGothicMedium';
  color: ${props => props.theme.colors.darkbluePrimaryColor};
`;

const FortuneWords = styled.div`
  width: 320px;
  height: 80px;
  padding: 5px;
  border: 10px solid #17355a;
  word-break: keep-all;
`;

const ModalBtns = styled.div`
  display: flex;
  justify-content: center;
  margin-top: 10px;
`;

const AgainBtn = styled.button`
  width: 120px;
  height: 30px;
  color: white;
  background-color: #ff495a;
  border: none;
  border-radius: 5px;
  margin-right: 5px;
  &:hover {
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.25);
  }
`;

const CaptureBtn = styled.button`
  width: 120px;
  height: 30px;
  color: white;
  background-color: #17355a;
  border: none;
  border-radius: 5px;
  &:hover {
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.25);
  }
`;
