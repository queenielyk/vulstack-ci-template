import Head from 'next/head';

function HomePage({ data }) {
  return (
    <div>
      <Head>
        <title>Vulnerable Next.js App</title>
      </Head>
      <h1>Welcome to the Vulnerable App</h1>
      {data && <p>Data from API: {data.message}</p>}
    </div>
  );
}

HomePage.getInitialProps = async () => {
  const res = await fetch(process.env.NEXT_PUBLIC_API_BASE_URL + '/data');
  const data = await res.json();
  return { data };
};

export default HomePage;
