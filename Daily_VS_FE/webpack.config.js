const path = require('path');

module.exports = {
  // ... 다른 설정 ...

  resolve: {
    alias: {
      '@api': path.resolve(__dirname, 'src/api'), // 실제 경로에 맞게 수정
    },
  },
};
