import type { Metadata } from "next";
import "./globals.css";
import { SpeechProvider } from "@/context/SpeechContext";
import SpeakableToggle from "@/components/SpeakableToggle";

export const metadata: Metadata = {
	title: "Sustainabite",
	description: "Sustainabite",
};

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return (
		<html lang="en">
			<body>
				<SpeechProvider>
					{children}
					<SpeakableToggle />
				</SpeechProvider>
			</body>
		</html>
	);
}
