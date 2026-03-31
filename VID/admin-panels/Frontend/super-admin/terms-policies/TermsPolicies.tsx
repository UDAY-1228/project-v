import React, { useState } from 'react';

interface TermsData {
  terms: string;
  privacy: string;
  agreements: string;
}

const TermsPolicies: React.FC = () => {
  const [termsData] = useState<TermsData>({
    terms: 'Terms and Conditions content...',
    privacy: 'Privacy Policy content...',
    agreements: 'Institution Agreements content...'
  });

  return (
    <div className="terms-policies-page">
      <h1>Terms & Policies</h1>
      <section>
        <h2>Terms and Conditions</h2>
        <p>{termsData.terms}</p>
      </section>
      <section>
        <h2>Privacy Policy</h2>
        <p>{termsData.privacy}</p>
      </section>
      <section>
        <h2>Institution Agreements</h2>
        <p>{termsData.agreements}</p>
      </section>
    </div>
  );
};

export default TermsPolicies;
