/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./**/*.html",
    "./assets/js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          dark: '#102A43',
          navy: '#0B1D30',
          blue: '#1677D2',
          'blue-hover': '#125ea7',
          cyan: '#35C6F4',
          'cyan-light': '#E8F8FE',
          light: '#F4F8FC',
          muted: '#627D98',
          border: '#D9E2EC',
          cta: '#F59E0B',
          'cta-hover': '#D97706',
          success: '#10B981',
          whatsapp: '#25D366',
          'whatsapp-hover': '#1EBE5D'
        }
      },
      fontFamily: {
        cairo: ['Cairo', 'Tajawal', 'system-ui', '-apple-system', 'sans-serif'],
        tajawal: ['Tajawal', 'Cairo', 'system-ui', '-apple-system', 'sans-serif']
      },
      boxShadow: {
        'soft': '0 4px 20px -2px rgba(16, 42, 67, 0.08)',
        'card': '0 10px 30px -5px rgba(16, 42, 67, 0.08), 0 4px 10px -2px rgba(16, 42, 67, 0.03)',
        'glow': '0 0 25px rgba(53, 198, 244, 0.35)'
      }
    },
  },
  plugins: [],
}
