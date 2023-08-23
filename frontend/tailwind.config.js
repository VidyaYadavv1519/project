/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {},
    colors: {
      light: {
          primary: {
          DEFAULT: '#2C00CC',
          100: '#463EC5',
          200: '#5F7BBD',
        },

      },
      dark: {
        DEFAULT: '#55B3FF',
          100: '#0A91FF',
          200: '#0065B8',
      },
    }
  },
  plugins: [],
};
