import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Nav from './components/Nav/Nav';
import Footer from './components/Footer/Footer';
import Main from './pages/Main/Main';
import Fortune from './pages/Fortune/Fortune';
import VoteDetail from './pages/Detail/Detail';
import VoteResult from './pages/Result/Result';
import DetailGender from './pages/Detail/DetailGender';
import DetailMBTI from './pages/Detail/DetailMBTI';
import Mypage from './pages/Mypage/Mypage';

const RouteWithNavFooter = () => {
  return (
    <>
      <Nav />
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/vote-detail/:id" element={<VoteDetail />} />
        <Route path="/vote-detail-gender/:id" element={<DetailGender />} />
        <Route path="/vote-detail-mbti/:id" element={<DetailMBTI />} />
        <Route path="/vote-result/:id" element={<VoteResult />} />
        <Route path="/fortune" element={<Fortune />} />
        <Route path="/my-page" element={<Mypage />} />
      </Routes>
      <Footer />
    </>
  );
};

export default RouteWithNavFooter;
