/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./critikeye_app/templates/**/*.html',
    './critikeye_app/static/js/**/*.js',],
  theme: {
    extend: {
      colors: {
        secondary:"#3A2161",
        green_secondary: "#00FFC2",
      },
      backgroundImage: {
        'star': "url('../images/star.svg')",
      }
    },
  },
  plugins: [],
}

