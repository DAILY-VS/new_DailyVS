// PollDetail.js

import React, { useState } from 'react';
import { toggleLike } from '../api/api';

function PollDetail({ poll }) {
  const [likes, setLikes] = useState(poll.likes);
  const [userLikesPoll, setUserLikesPoll] = useState(poll.user_likes_poll);

  const handleLikeClick = async () => {
    try {
      const data = await toggleLike(poll.id);
      setLikes(data.like_count);
      setUserLikesPoll(data.user_likes_poll);
    } catch (error) {
      console.error('Error toggling like:', error);
    }
  };

  return (
    <div>
      <h2>{poll.title}</h2>
      <p>Likes: {likes}</p>
      <button onClick={handleLikeClick}>
        {userLikesPoll ? '좋아요 취소' : '좋아요'}
      </button>
    </div>
  );
}

export default PollDetail;
