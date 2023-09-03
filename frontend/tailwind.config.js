/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {},
    colors: {
      light: {
        main: {
          DEFAULT: "#FFFFFF",
          100: "#F1F5F9",
          200: "#E2E8F0",
        },
        primary: {
          DEFAULT: "#2C00CC",
          100: "#463EC5",
          200: "#5F7BBD",
        },
      },
      dark: {
        main: {
          DEFAULT: "#000000",
          100: "#0F172A",
          200: "#1E293B",
        },
        primary: {
          DEFAULT: "#55B3FF",
          100: "#0A91FF",
          200: "#0065B8",
        },
      },
    },
  },
  plugins: [],
};
