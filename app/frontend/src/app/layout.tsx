import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import localFont from 'next/font/local'
import Image from "next/image";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar" /*Importinh avatar from shadcn */
import Footerwave from "../../public/Footer_Wave.svg"; /*Imporrting the wave svg */

const inter = Inter({ subsets: ["latin"] });
const Virgil = localFont({ src: './Virgil.woff2' }) /*Importing the virgol font */

export const metadata: Metadata = {
  title: "AcademyX",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body >
        <main className={Virgil.className}>{/*Virgil is the font used for the academy x logo */}
        <header className="w-screen h-1/6 flex justify-between items-center border-academy bg-black  border-2 rounded-b-sm border-t-0">
          <div className=" p-2">{/*This div will have the hamburger menu, which i have yet not worked on */}

          </div>
          <div className=" p-2 flex justify-start text-lg">{/*This div has the AcademyX text aka our logo*/}
          <p    className=" text-white">Academy</p>
          <p    className=" text-academy">X</p>
          </div>
          <div className=" p-2">{/*This div has the avatar properties */}
            <Avatar>
              <AvatarImage src="https://github.com/shadcn.png" />
              <AvatarFallback>CN</AvatarFallback>
            </Avatar>
          </div>
        </header>
        </main>
        {children}
        <footer className="bottom-0 relative w-screen">
          <div className="flex justify-start relative z-0">
          <Image src={Footerwave} alt="Footerbg" className="w-screen"/>
          <div className=" absolute bottom-0 z-10 w-screen h-3/5 ">
            {/*footer contet goes in this div, idk what to write here*/}
            <p className="px-2"><strong>AcademyX</strong> <br /> Webstie created by ACM PESU ECC <br />-this website is open source</p>
          <h1 className="px-2">Contact us: <br /></h1>
          <div className="flex justify-start items-center w-1/6 p-2">
          <a target="_blank" href="https://github.com/acmpesuecc/AcademyX/">
          <img src="https://skillicons.dev/icons?i=github" /></a>
          <a href="https://skillicons.dev">
          <img src="https://skillicons.dev/icons?i=gmail" /></a>
          <a href="https://skillicons.dev">
          <img src="https://skillicons.dev/icons?i=linkedin" /></a>
          </div> 
            <p className="tet-2xl absolute bottom-10 right-10">&copy; ACMPESUECC</p>
          </div>
          </div>
          
        </footer>
        
        </body>
    </html>
  );
}