/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Type errors still fail the build; we only skip lint to avoid requiring an
  // ESLint install in CI/Render. Run `npm run lint` locally if desired.
  eslint: { ignoreDuringBuilds: true },
};

export default nextConfig;
